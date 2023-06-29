import streamlit as st

st.title('纳尼说Nanitalk')
st.header('呆鸟日记') 
st.image('IMG_2653.jpeg')
st.markdown('这是一部超级有趣的动画电影......')

st.header('纳尼说') 
st.image('IMG_2653.jpeg')
st.markdown('这是一部超级有趣的动画电影......')

st.header('虎克虎克！') 
st.image('IMG_2653.jpeg')
st.markdown('这是一部超级有趣的动画电影......')


option = st.selectbox('选择一个漫画:', ['纳尼说Nanitalk', '呆鸟日记', '虎克虎克！']) 
if option == '纳尼说Nanitalk':
   st.image('IMG_2653.jpeg')
elif option == '呆鸟日记':
   st.image('IMG_2653.jpeg')
else:
   st.image('IMG_2653.jpeg')
