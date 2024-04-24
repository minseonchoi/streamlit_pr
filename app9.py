# 차트 그리는 방법

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main() :
    st.title('차트 크리기 1')

    df = pd.read_csv('./data/iris.csv')

    st.dataframe(df)

    # sepal_length 와 sepal_width 의 두 컬럼 간의 관계를 차트로 나타내시오.
    # 메트플롯의 scatter
    fig1 = plt.figure()
    plt.scatter(data= df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length VS Width')
    st.pyplot(fig1)

    # 시본의 scatterplot
    fig2 = plt.figure()
    sb.scatterplot(data= df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length VS Width')    
    st.pyplot(fig2)

    # 시본의 regplot 
    fig3 = plt.figure()
    sb.regplot(data= df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length VS Width')    
    st.pyplot(fig3)

    # sepal_length 로 히스토 그램을 그린다
    # bins 의 갯수는 20개로
    fig4 = plt.figure()
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.9)
    plt.title('Histogram')
    plt.xlabel('sepal_length')
    plt.ylabel('count')
    st.pyplot(fig4)

    # sepal_length 히스토그램을 그리되,
    # bins 의 갯수를 10개와 20개로 두개의 차트를 수평으로 보여주세요.
    fig5 = plt.figure(figsize=(10,4))

    plt.subplot(1, 2, 1)
    plt.hist(data=df, x='sepal_length', bins=10, rwidth=0.9)
    plt.title('Histogram')
    plt.xlabel('sepal_length')
    plt.ylabel('count')

    plt.subplot(1, 2, 2)
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.9)
    plt.title('Histogram')
    plt.xlabel('sepal_length')
    plt.ylabel('count')

    st.pyplot(fig5)

    # 판다스의 데이터프레임의 차트도 그릴 수 있다.

    # species 는 몇개인지 나타내시오
    print(df['species'].value_counts())
    
    # 위의 결과를 바차트로 나타내시오
    fig6 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig6)

    # sepal_length 컬럼을 히스토그램으로 나타내시오.
    # 데이터프레임의 차트그리는 함수
    fig7 = plt.figure()
    df['sepal_length'].hist(rwidth=0.9)
    st.pyplot(fig7)

    # df 의 상관계수를 구해서, 차트로 표시
    cor = df.corr(numeric_only=True)
    fig8 = plt.figure()
    sb.heatmap(cor, vmin=-1, vmax=1, annot=True, fmt='.1f', cmap='Blues')
    st.pyplot(fig8)



if __name__ == '__main__':
    main()

