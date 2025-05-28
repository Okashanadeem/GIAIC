import streamlit as st
from inventory import Electronics, Grocery, Clothing, Inventory, OutOfStockError, DuplicateProductIDError

# --- Page Configuration ---
st.set_page_config(page_title="Inventory Manager", page_icon="📦", layout="centered")

# --- Initialize Inventory (per session) ---
if "inv" not in st.session_state:
    st.session_state.inv = Inventory()
inv = st.session_state.inv

# --- Sidebar Controls ---
st.sidebar.title("🔧 Inventory Controls")
action = st.sidebar.selectbox("Choose an Action", [
    "📋 View All Products", "➕ Add Product", "📉 Sell Product", 
    "📦 Restock Product", "💾 Save Inventory", 
    "📂 Load Inventory", "🗑️ Remove Expired Items"
])

# --- Action Handlers ---
if action == "💾 Save Inventory":
    filename = st.sidebar.text_input("Enter filename", "inventory.json")
    if st.sidebar.button("Save"):
        inv.save_to_file(filename)
        st.sidebar.success(f"Inventory saved to **{filename}** ✅")

elif action == "📂 Load Inventory":
    uploaded = st.sidebar.file_uploader("Upload inventory file (JSON)", type="json")
    if uploaded:
        inv.load_from_file(uploaded)
        st.sidebar.success("Inventory loaded successfully ✅")

elif action == "➕ Add Product":
    st.sidebar.markdown("### Product Details")
    ptype = st.sidebar.selectbox("Category", ["Electronics", "Grocery", "Clothing"])
    pid = st.sidebar.text_input("Product ID")
    name = st.sidebar.text_input("Product Name")
    price = st.sidebar.number_input("Price ($)", min_value=0.0, format="%.2f")
    qty = st.sidebar.number_input("Quantity in Stock", min_value=0, step=1)

    if ptype == "Electronics":
        warr = st.sidebar.number_input("Warranty (Years)", min_value=0, step=1)
        brand = st.sidebar.text_input("Brand")
        if st.sidebar.button("Add Electronics"):
            try:
                inv.add_product(Electronics(pid, name, price, qty, warr, brand))
                st.sidebar.success("✅ Electronics product added!")
            except DuplicateProductIDError as e:
                st.sidebar.error(f"❌ {e}")

    elif ptype == "Grocery":
        exp = st.sidebar.date_input("Expiry Date")
        if st.sidebar.button("Add Grocery"):
            try:
                inv.add_product(Grocery(pid, name, price, qty, exp.isoformat()))
                st.sidebar.success("✅ Grocery product added!")
            except DuplicateProductIDError as e:
                st.sidebar.error(f"❌ {e}")

    else:  # Clothing
        size = st.sidebar.text_input("Size (e.g. M, L)")
        mat = st.sidebar.text_input("Material")
        if st.sidebar.button("Add Clothing"):
            try:
                inv.add_product(Clothing(pid, name, price, qty, size, mat))
                st.sidebar.success("✅ Clothing product added!")
            except DuplicateProductIDError as e:
                st.sidebar.error(f"❌ {e}")

elif action in ("📉 Sell Product", "📦 Restock Product"):
    pid = st.sidebar.text_input("Enter Product ID")
    qty = st.sidebar.number_input("Quantity", min_value=1, step=1)
    label = "Sell" if action == "📉 Sell Product" else "Restock"
    if st.sidebar.button(label):
        try:
            if label == "Sell":
                inv.sell_product(pid, qty)
            else:
                inv.restock_product(pid, qty)
            st.sidebar.success(f"✅ {label} successful!")
        except (KeyError, OutOfStockError) as e:
            st.sidebar.error(f"❌ {e}")

elif action == "🗑️ Remove Expired Items":
    if st.sidebar.button("Remove Now"):
        inv.remove_expired_products()
        st.sidebar.success("✅ Expired groceries removed.")

# --- Main Dashboard ---
st.title("📦 Inventory Management Dashboard")
st.markdown("Welcome to your **smart inventory system**. Keep your products organized and your stock up-to-date.")

# ✅ Total Inventory Value
st.metric("💰 Total Inventory Value", f"${inv.total_value():.2f}")

# 🔍 Search Products
search = st.text_input("🔍 Search products by name (case-insensitive)")
if search:
    results = inv.search_by_name(search)
    if not results:
        st.warning("No products found.")
else:
    results = inv.list_all_products()

# 📋 Display Products
for product in results:
    with st.expander(f"🧾 {product.name} (ID: {product.product_id})"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Category**: {type(product).__name__}")
            st.write(f"**Price**: ${product.price:.2f}")
            st.write(f"**Stock**: {product.quantity}")
        with col2:
            for attr, value in product.__dict__.items():
                if attr not in ("product_id", "name", "price", "quantity"):
                    st.write(f"**{attr.replace('_', ' ').title()}**: {value}")
