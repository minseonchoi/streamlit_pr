# 파일을 분리해서 개발하는 방법
# 장점 :
# 여러 사람이 동시에 개발을 할수 있다 협업을 할 수 있다
# 디버그를 쉽게 할 수 있다 어느 부분을 찾아야 하는지를 쉽게 다룰 수 있다
# 유지 보수가 쉽다

import streamlit as st
# 다른 파일로 분리한 라이브러리 이렇게 만드는 것이다
from app8_home import run_home
from app8_eda import run_eda
from app8_ml import run_ml
from app8_about import run_about

def main() :
    st.title('파일 분리 앱')

    # 사이드 바 만들기
    menu = ['Home','EDA','ML','About']
    choice = st.sidebar.selectbox( '메뉴', menu )
    if choice == menu[0]:
        # 다른 파일 만들고 라이브러리로 함수 가져다 쓴다
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()
    elif choice == menu[3]:
        run_about()




if __name__ == '__main__':
    main()
