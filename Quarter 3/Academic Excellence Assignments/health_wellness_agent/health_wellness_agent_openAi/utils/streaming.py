"""
Streaming utilities for Health & Wellness Planner Agent
Handles real-time streaming of agent responses and tool outputs
"""

import asyncio
import json
import logging
from typing import AsyncIterator, Dict, Any, Optional, List, Union
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StreamingEventType(Enum):
    """Types of streaming events"""
    AGENT_START = "agent_start"
    AGENT_END = "agent_end"
    TOOL_START = "tool_start"
    TOOL_END = "tool_end"
    HANDOFF = "handoff"
    MESSAGE = "message"
    ERROR = "error"
    PROGRESS = "progress"

@dataclass
class StreamingConfig:
    """Configuration for streaming behavior"""
    buffer_size: int = 1024
    flush_interval: float = 0.1
    include_metadata: bool = True
    format_json: bool = True
    show_tool_calls: bool = True
    show_progress: bool = True
    error_handling: str = "continue"  # "continue", "stop", "retry"

class StreamingHandler:
    """
    Handles streaming responses from agents and tools
    Provides real-time output formatting and error handling
    """
    
    def __init__(self, config: Optional[StreamingConfig] = None):
        self.config = config or StreamingConfig()
        self.buffer = []
        self.last_flush = datetime.now()
        self.event_count = 0
        self.error_count = 0
        
    async def process_stream(self, stream: AsyncIterator[Dict[str, Any]]) -> AsyncIterator[str]:
        """
        Process streaming events and yield formatted responses
        """
        try:
            async for event in stream:
                self.event_count += 1
                
                # Handle different event types
                formatted_output = await self._format_event(event)
                
                if formatted_output:
                    # Add to buffer
                    self.buffer.append(formatted_output)
                    
                    # Check if we should flush
                    if await self._should_flush():
                        async for output in self._flush_buffer():
                            yield output
                        
        except Exception as e:
            logger.error(f"Error in streaming: {e}")
            self.error_count += 1
            
            if self.config.error_handling == "stop":
                raise
            elif self.config.error_handling == "continue":
                yield await self._format_error(e)
            # For retry, we could implement retry logic here
            
        # Final flush
        async for output in self._flush_buffer():
            yield output
    
    async def _format_event(self, event: Dict[str, Any]) -> Optional[str]:
        """
        Format a single streaming event
        """
        event_type = event.get("type", "unknown")
        timestamp = datetime.now().isoformat()
        
        # Handle different event types
        if event_type == StreamingEventType.AGENT_START.value:
            return await self._format_agent_start(event, timestamp)
        elif event_type == StreamingEventType.AGENT_END.value:
            return await self._format_agent_end(event, timestamp)
        elif event_type == StreamingEventType.TOOL_START.value and self.config.show_tool_calls:
            return await self._format_tool_start(event, timestamp)
        elif event_type == StreamingEventType.TOOL_END.value and self.config.show_tool_calls:
            return await self._format_tool_end(event, timestamp)
        elif event_type == StreamingEventType.HANDOFF.value:
            return await self._format_handoff(event, timestamp)
        elif event_type == StreamingEventType.MESSAGE.value:
            return await self._format_message(event, timestamp)
        elif event_type == StreamingEventType.PROGRESS.value and self.config.show_progress:
            return await self._format_progress(event, timestamp)
        elif event_type == StreamingEventType.ERROR.value:
            return await self._format_error_event(event, timestamp)
        
        return None
    
    async def _format_agent_start(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format agent start event"""
        agent_name = event.get("agent_name", "Unknown Agent")
        
        if self.config.format_json:
            return json.dumps({
                "type": "agent_start",
                "agent": agent_name,
                "timestamp": timestamp,
                "message": f"🤖 {agent_name} is thinking..."
            }) + "\n"
        else:
            return f"🤖 {agent_name} is thinking...\n"
    
    async def _format_agent_end(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format agent end event"""
        agent_name = event.get("agent_name", "Unknown Agent")
        
        if self.config.format_json:
            return json.dumps({
                "type": "agent_end",
                "agent": agent_name,
                "timestamp": timestamp,
                "message": f"✅ {agent_name} completed"
            }) + "\n"
        else:
            return f"✅ {agent_name} completed\n"
    
    async def _format_tool_start(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format tool start event"""
        tool_name = event.get("tool_name", "Unknown Tool")
        
        if self.config.format_json:
            return json.dumps({
                "type": "tool_start",
                "tool": tool_name,
                "timestamp": timestamp,
                "message": f"🔧 Using {tool_name}..."
            }) + "\n"
        else:
            return f"🔧 Using {tool_name}...\n"
    
    async def _format_tool_end(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format tool end event"""
        tool_name = event.get("tool_name", "Unknown Tool")
        result = event.get("result", {})
        
        if self.config.format_json:
            return json.dumps({
                "type": "tool_end",
                "tool": tool_name,
                "timestamp": timestamp,
                "result": result,
                "message": f"✅ {tool_name} completed"
            }) + "\n"
        else:
            return f"✅ {tool_name} completed\n"
    
    async def _format_handoff(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format handoff event"""
        from_agent = event.get("from_agent", "Unknown")
        to_agent = event.get("to_agent", "Unknown")
        reason = event.get("reason", "No reason provided")
        
        if self.config.format_json:
            return json.dumps({
                "type": "handoff",
                "from": from_agent,
                "to": to_agent,
                "reason": reason,
                "timestamp": timestamp,
                "message": f"🔄 Transferring from {from_agent} to {to_agent}"
            }) + "\n"
        else:
            return f"🔄 Transferring from {from_agent} to {to_agent}\n   Reason: {reason}\n"
    
    async def _format_message(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format message event"""
        content = event.get("content", "")
        sender = event.get("sender", "Assistant")
        
        if self.config.format_json:
            return json.dumps({
                "type": "message",
                "sender": sender,
                "content": content,
                "timestamp": timestamp
            }) + "\n"
        else:
            return f"💬 {sender}: {content}\n"
    
    async def _format_progress(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format progress event"""
        progress = event.get("progress", 0)
        step = event.get("step", "")
        total_steps = event.get("total_steps", 100)
        
        progress_bar = "█" * int(progress / 10) + "░" * (10 - int(progress / 10))
        
        if self.config.format_json:
            return json.dumps({
                "type": "progress",
                "progress": progress,
                "step": step,
                "total_steps": total_steps,
                "timestamp": timestamp,
                "message": f"📊 Progress: {progress}% [{progress_bar}] {step}"
            }) + "\n"
        else:
            return f"📊 Progress: {progress}% [{progress_bar}] {step}\n"
    
    async def _format_error_event(self, event: Dict[str, Any], timestamp: str) -> str:
        """Format error event"""
        error_msg = event.get("error", "Unknown error")
        
        if self.config.format_json:
            return json.dumps({
                "type": "error",
                "error": error_msg,
                "timestamp": timestamp,
                "message": f"❌ Error: {error_msg}"
            }) + "\n"
        else:
            return f"❌ Error: {error_msg}\n"
    
    async def _format_error(self, error: Exception) -> str:
        """Format a general error"""
        timestamp = datetime.now().isoformat()
        
        if self.config.format_json:
            return json.dumps({
                "type": "error",
                "error": str(error),
                "timestamp": timestamp,
                "message": f"❌ Streaming error: {str(error)}"
            }) + "\n"
        else:
            return f"❌ Streaming error: {str(error)}\n"
    
    async def _should_flush(self) -> bool:
        """Check if buffer should be flushed"""
        now = datetime.now()
        time_since_flush = (now - self.last_flush).total_seconds()
        
        return (len(self.buffer) >= self.config.buffer_size or 
                time_since_flush >= self.config.flush_interval)
    
    async def _flush_buffer(self) -> AsyncIterator[str]:
        """Flush the buffer and yield all contents"""
        if not self.buffer:
            return
            
        for item in self.buffer:
            yield item
        
        self.buffer.clear()
        self.last_flush = datetime.now()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get streaming statistics"""
        return {
            "events_processed": self.event_count,
            "errors_encountered": self.error_count,
            "buffer_size": len(self.buffer),
            "last_flush": self.last_flush.isoformat()
        }

# Utility functions
async def format_streaming_response(response: Dict[str, Any], 
                                  config: Optional[StreamingConfig] = None) -> str:
    """
    Format a single streaming response
    """
    handler = StreamingHandler(config)
    return await handler._format_event(response)

async def handle_streaming_errors(stream: AsyncIterator[Dict[str, Any]], 
                                error_callback: Optional[callable] = None) -> AsyncIterator[Dict[str, Any]]:
    """
    Handle errors in streaming with optional callback
    """
    try:
        async for event in stream:
            yield event
    except Exception as e:
        logger.error(f"Streaming error: {e}")
        if error_callback:
            await error_callback(e)
        
        # Yield error event
        yield {
            "type": StreamingEventType.ERROR.value,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

def create_streaming_context(user_id: str, session_id: str) -> Dict[str, Any]:
    """
    Create a streaming context for tracking user sessions
    """
    return {
        "user_id": user_id,
        "session_id": session_id,
        "start_time": datetime.now().isoformat(),
        "events": [],
        "metadata": {
            "streaming_version": "1.0.0",
            "created_by": "Health & Wellness Planner"
        }
    }

class StreamingBuffer:
    """
    A buffer for collecting streaming events before processing
    """
    
    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.events: List[Dict[str, Any]] = []
        self.lock = asyncio.Lock()
    
    async def add_event(self, event: Dict[str, Any]) -> None:
        """Add an event to the buffer"""
        async with self.lock:
            self.events.append(event)
            if len(self.events) > self.max_size:
                self.events.pop(0)  # Remove oldest event
    
    async def get_events(self, count: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get events from the buffer"""
        async with self.lock:
            if count is None:
                return self.events.copy()
            else:
                return self.events[-count:].copy()
    
    async def clear(self) -> None:
        """Clear the buffer"""
        async with self.lock:
            self.events.clear()
    
    def size(self) -> int:
        """Get current buffer size"""
        return len(self.events)

# Example usage
async def example_streaming_usage():
    """
    Example of how to use the streaming utilities
    """
    config = StreamingConfig(
        buffer_size=10,
        flush_interval=0.5,
        include_metadata=True,
        format_json=True
    )
    
    handler = StreamingHandler(config)
    
    # Mock streaming events
    events = [
        {"type": "agent_start", "agent_name": "HealthPlannerAgent"},
        {"type": "message", "content": "Hello! I'm analyzing your goals...", "sender": "Assistant"},
        {"type": "tool_start", "tool_name": "GoalAnalyzerTool"},
        {"type": "tool_end", "tool_name": "GoalAnalyzerTool", "result": {"goal": "weight_loss"}},
        {"type": "agent_end", "agent_name": "HealthPlannerAgent"}
    ]
    
    async def mock_stream():
        for event in events:
            await asyncio.sleep(0.1)  # Simulate streaming delay
            yield event
    
    # Process the stream
    async for output in handler.process_stream(mock_stream()):
        print(output.strip())
    
    # Show stats
    stats = handler.get_stats()
    print(f"\nStreaming Stats: {stats}")

if __name__ == "__main__":
    # Run example
    asyncio.run(example_streaming_usage())