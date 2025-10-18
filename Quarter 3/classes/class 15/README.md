class 15

we learnt about these special values

name_override="get_weather",
description_override="weather ka data le ao.",
use_docstring_info=False

open-ai by default pass a function called default_tool_error_function when a crash occur in a tool call
it could be user erorr, model error etc.
if we give value none then it will give error or raise the error which you have made by your self
we can create our own failure error and run it when the tool crashes

we learnt agent as tool where we use a specialize agent as a tool

what is custom_output_extractor?
custom_output_extractor is a function which is used to extract the output from the tool response. It is used to customize the output of the tool.

how to make a tool from custom class?
class CustomTool:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def as_tool(self):
        return {
            "name": self.name,
            "description": self.description,
            "function": self.custom_function
        }

    def custom_function(self, input_data):
        # Custom logic here
        return {"result": f"Processed {input_data}"}

whay would we use the tool made of custom class?


what is on_handoff()
customzing the handoff using handoff()

we made a on hand off function which basically fetch the data from the input and show that what basically user want.

what is input_filter?
input_filter is a function which is used to filter the input before passing it to the tool.