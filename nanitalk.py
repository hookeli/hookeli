import streamlit as st

st.title('纳尼说Nanitalk')
st.header('呆鸟日记') 
st.image('/Users/apple/Documents/绘画手稿/春游日.jpg')
st.markdown('这是一部超级有趣的动画电影......')

st.header('纳尼说') 
st.image('/Users/apple/Documents/绘画手稿/0316小浣熊.jpg')
st.markdown('这是一部超级有趣的动画电影......')

st.header('虎克虎克！') 
st.image('/Users/apple/Documents/绘画手稿/6541647874457_.pic.jpg')
st.markdown('这是一部超级有趣的动画电影......')


option = st.selectbox('选择一个漫画:', ['纳尼说Nanitalk', '呆鸟日记', '虎克虎克！']) 
if option == '纳尼说Nanitalk':
   st.image('/Users/apple/Documents/绘画手稿/春游日.jpg')
elif option == '呆鸟日记':
   st.image('/Users/apple/Documents/绘画手稿/0316小浣熊.jpg')
else:
    st.image('/Users/apple/Documents/绘画手稿/6541647874457_.pic.jpg')
