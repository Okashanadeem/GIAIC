import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

# Initialize session state for library if it doesn't exist
if 'library' not in st.session_state:
    st.session_state.library = []

def save_library():
    """Save the library to a JSON file"""
    with open('library.json', 'w', encoding='utf-8') as f:
        json.dump(st.session_state.library, f, indent=4, ensure_ascii=False)

def load_library():
    """Load the library from a JSON file"""
    if os.path.exists('library.json'):
        with open('library.json', 'r', encoding='utf-8') as f:
            st.session_state.library = json.load(f)

def add_book(title, author, year, genre, read_status):
    """Add a new book to the library"""
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read_status': read_status,
        'date_added': datetime.now().strftime("%Y-%m-%d")
    }
    st.session_state.library.append(book)
    save_library()
    return True

def remove_book(title):
    """Remove a book from the library by title"""
    st.session_state.library = [book for book in st.session_state.library if book['title'].lower() != title.lower()]
    save_library()
    return True

def search_books(query, search_by='title'):
    """Search for books by title or author"""
    query = query.lower()
    if search_by == 'title':
        return [book for book in st.session_state.library if query in book['title'].lower()]
    else:
        return [book for book in st.session_state.library if query in book['author'].lower()]

def get_statistics():
    """Calculate library statistics"""
    total_books = len(st.session_state.library)
    if total_books == 0:
        return 0, 0
    read_books = sum(1 for book in st.session_state.library if book['read_status'])
    percentage_read = (read_books / total_books) * 100
    return total_books, percentage_read

def main():
    st.set_page_config(page_title="Personal Library Manager", page_icon="📚")
    
    # Load existing library
    load_library()
    
    st.title("📚 Personal Library Manager")
    
    # Create tabs for different functions
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Add Book", "Remove Book", "Search Books", "View Library", "Statistics"])
    
    with tab1:
        st.header("Add New Book")
        with st.form("add_book_form"):
            title = st.text_input("Title")
            author = st.text_input("Author")
            year = st.number_input("Publication Year", min_value=1800, max_value=datetime.now().year)
            genre = st.text_input("Genre")
            read_status = st.checkbox("I have read this book")
            
            if st.form_submit_button("Add Book"):
                if title and author and genre:
                    if add_book(title, author, year, genre, read_status):
                        st.success("Book added successfully!")
                        st.balloons()
                else:
                    st.error("Please fill in all required fields!")
    
    with tab2:
        st.header("Remove Book")
        if st.session_state.library:
            book_to_remove = st.selectbox(
                "Select book to remove",
                options=[book['title'] for book in st.session_state.library]
            )
            if st.button("Remove Book"):
                if remove_book(book_to_remove):
                    st.success("Book removed successfully!")
        else:
            st.info("Your library is empty!")
    
    with tab3:
        st.header("Search Books")
        search_by = st.radio("Search by:", ["Title", "Author"])
        search_query = st.text_input("Enter search term")
        
        if search_query:
            results = search_books(search_query, search_by.lower())
            if results:
                st.write(f"Found {len(results)} matching books:")
                for book in results:
                    st.write(f"- {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read_status'] else 'Unread'}")
            else:
                st.info("No matching books found!")
    
    with tab4:
        st.header("View Library")
        if st.session_state.library:
            # Convert library to DataFrame for better display
            df = pd.DataFrame(st.session_state.library)
            df['read_status'] = df['read_status'].map({True: 'Read', False: 'Unread'})
            st.dataframe(df)
        else:
            st.info("Your library is empty!")
    
    with tab5:
        st.header("Library Statistics")
        total_books, percentage_read = get_statistics()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Books", total_books)
        with col2:
            st.metric("Percentage Read", f"{percentage_read:.1f}%")
        
        if total_books > 0:
            # Create a pie chart of read vs unread books
            read_count = sum(1 for book in st.session_state.library if book['read_status'])
            unread_count = total_books - read_count
            
            chart_data = pd.DataFrame({
                'Status': ['Read', 'Unread'],
                'Count': [read_count, unread_count]
            })
            
            st.bar_chart(chart_data.set_index('Status'))
            
            # Display genre distribution
            genre_counts = pd.DataFrame(st.session_state.library)['genre'].value_counts()
            st.subheader("Genre Distribution")
            st.bar_chart(genre_counts)
    
    # Footer with additional information
    st.markdown("---")
    st.markdown("""
    ### 💡 Tips
    - Keep your library organized by regularly updating read status
    - Use the search feature to quickly find books
    - Check statistics to track your reading progress
    - Your library is automatically saved
    """)

if __name__ == "__main__":
    main()
