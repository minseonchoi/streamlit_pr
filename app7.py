# 파일을 업로드 하는 방법
# 이미지 파일 업로드, csv 파일 업로드

import streamlit as st
# 현재 시간을 가져와서 유니크한 파일 명을 만드는데 사용하기 위해서 했다
from datetime import datetime
import pandas as pd
from PIL import Image

# 디렉토리 정보와, 파일을 알려주면, 
# 해당 디렉토리에 파일을 저장하는 함수
def save_uploaded_file(directory, file) :
    # 1. 디렉토리가 있는지 확인하여, 없으면 디렉토리 부터 만든다.
    import os
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 존재하면, 파일을 저장하다.
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    # 3. 저장이 완료되면, 유저한테 알린다.
    return st.success(f"{file.name} 이 {directory} 에 저장 되었습니다.")


def main() :
    # 사이드바 만들기
    st.title('파일 업로드 프로젝트')

    # 깔금한 코드
    menu = ['이미지파일 업로드', 'csv 업로드', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)
    print(choice)

    if choice == menu[0]:
        # 순서를 정해두고 코드를 짠다 로직을 짠다
        # 1. 부 제목
        st.subheader('이미지 파일 업로드!')

        # 2. 파일 선택하기 후 메모리에 저장하기
        file = st.file_uploader('이미지 파일 선택하세요.', type=['jpg','png','jpeg'])

        # 3. 우리 서버에 저장하기
        # 유저가 올린 파일이 있을때만, 서버에 저장한다.
        if file is not None :
            print(file.name)
            print(file.size)
            print(file.type)
            
            # 파일을 서버에 저장하기 위해서 먼저!
            # 서버에서 관리 하기 쉽도록 
            # 파일 이름을 유니크하게 만들어서 바꿔줘야 한다.
            # 실무에서 가장 많이! 현재시간과 유저의 아이디를 조합해서 만든다
            current_time = datetime.now()
            print(current_time)

            # 파일명으로 저장해줘야 하니 문자열로 바꾼다 
            # 파일명이 클론이 들어가서 다른 것으로 대체 해야한다
            print(current_time.isoformat().replace(':','_') + '.jpg')

            new_filename = current_time.isoformat().replace( ':','_' ) + '.jpg'
            file.name = new_filename

            save_uploaded_file( 'image', file )

            img = Image.open(file)
            st.image(img)
            # st.image(file) 도 사용 가능하다
        
    elif choice == menu[1]:
        st.subheader('CSV 파일 업로드')
        file = st.file_uploader('CSV 파일 선택하기.', type='csv')

        if file is not None :

            # 파일명을 유니크하게 만들어서 저장한다.
            current_time = datetime.now()

            print( current_time.isoformat().replace(":", "_") +".csv" )

            new_filename = current_time.isoformat().replace(":", "_") +".csv"

            file.name = new_filename

            save_uploaded_file("data", file)

            # print( pd.read_csv(file) )

            st.dataframe(pd.read_csv(file))


    elif choice == menu[2]:
        st.subheader('파일 업로드 프로젝트 입니다')






if __name__ == '__main__':
    main()