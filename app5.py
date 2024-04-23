# 이미지/동영상/음악파일 을 화면에 보여주는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리 파이썬이미지라이브러리PIL
from PIL import Image

def main() :
    # 1. 저장되어 있는 이미지 파일을 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg')
    
    st.image(img)

    st.image(img, width=600)

    st.image(img, use_column_width=True)

    # 2. 인터넷 상에 있는 이미지를 화면에 표시하는 방법
    #    인터넷 상의 이미지 : url 이 있다!!

    url = 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSM6HM1W3sF0CaA66OuR6lddF93hMGxjTnyr6h_7mReU1_AhTY6'
    st.image(url)

    
    # 동영상 파일
    video_file = open('./data/video1.mp4', 'rb')
    st.video(video_file)


    # 오디오 파일
    audio_file = open('./data/song.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')



if __name__ == '__main__':
    main()
