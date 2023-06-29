import streamlit as st

st.title('纳尼说Nanitalk')
st.header('呆鸟日记') 
st.image('/Users/apple/Desktop/AI/spider/nanitalk/IMG_2653.jpeg')
st.markdown('这是一部超级有趣的动画电影......')

st.header('纳尼说') 
st.image('/Users/apple/Desktop/AI/spider/nanitalk/IMG_2653.jpeg')
st.markdown('这是一部超级有趣的动画电影......')

st.header('虎克虎克！') 
st.image('/Users/apple/Desktop/AI/spider/nanitalk/0316小浣熊.jpg')
st.markdown('这是一部超级有趣的动画电影......')


option = st.selectbox('选择一个漫画:', ['纳尼说Nanitalk', '呆鸟日记', '虎克虎克！']) 
if option == '纳尼说Nanitalk':
   st.image('/Users/apple/Desktop/AI/spider/nanitalk/IMG_2653.jpeg')
elif option == '呆鸟日记':
   st.image('/Users/apple/Desktop/AI/spider/nanitalk/IMG_2653.jpeg')
else:
    st.image('/Users/apple/Desktop/AI/spider/nanitalk/0316小浣熊.jpg')
