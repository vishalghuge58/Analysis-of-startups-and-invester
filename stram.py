import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('startup_processed.csv',encoding='utf-8')
df['Date']=pd.to_datetime(df['Date'],errors='coerce')
startup_name=sorted(df['startup_name'].unique().tolist())

Investers=sorted(set(df['invester_name'].str.split(',').sum()))
df['year']=df['Date'].dt.year
df['month']=df['Date'].dt.month

st.set_page_config(layout='wide')

def details_invester(invester):

    temp_df=df[df['invester_name'].str.contains(invester)]

    st.title(invester)
    



    #  most recent five investments

    most_recent=temp_df.head()[[ 'Date', 'startup_name', 'subvertical',
       'city', 'investment_type', 'amount','year']]
    st.subheader('MOst Recent five Investments')
    st.dataframe(most_recent)



    # Biggest Investments
    big_series = temp_df.groupby('startup_name')['amount'].sum().sort_values(ascending=False).head()

    col1,col2=st.columns(2)
    with col1:
        st.subheader('Biggest Investments')
        st.dataframe(big_series)
            
       
    
    with col2:
        fig,ax=plt.subplots()
        st.subheader('Biggest Investments')
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)




    #industry_vertical/Sectorwise Investments

    col3,col4=st.columns(2)

    with col3:

        secter_wise=temp_df.groupby('industry_vertical').sum()['amount'].sort_values(ascending=False)
        st.subheader('secter_wise Investments')
        st.dataframe(secter_wise)
            
       
    
    with col4:
        fig,ax=plt.subplots()
        st.subheader("secter_wise Investments")
        ax.pie(secter_wise.values,labels=secter_wise.index,autopct="%0.01f%%")
        st.pyplot(fig)
        

    # investment_type

    col5,col6=st.columns(2)

    with col5:

        secter_wise=temp_df.groupby('investment_type').sum()['amount'].sort_values(ascending=False)
        st.subheader('Investment_type ')
        st.dataframe(secter_wise)
            
       
    
    with col6:
        fig,ax=plt.subplots()
        st.subheader("Investment Type")

        ax.pie(secter_wise.values,labels=secter_wise.index,autopct="%0.01f%%")
        st.pyplot(fig)        

    # City-wise Investments

    col7,col8=st.columns(2)

    city_wise=temp_df.groupby('city')['amount'].sum().sort_values(ascending=False)

    with col7:
        st.subheader("city-Wise Investments")
        st.dataframe(city_wise)

    with col8:
        fig,ax=plt.subplots()
        st.subheader("city-Wise Investments")
        ax.bar(city_wise.index,city_wise.values)
        # print(year_wise)
        st.pyplot(fig)


    # Years-wise Investments

    col7,col8=st.columns(2)

    year_wise=temp_df.groupby('year')['amount'].sum().sort_values(ascending=False)

    with col7:
        st.subheader("Year-Wise Investments")
        st.dataframe(year_wise)

    with col8:
        fig,ax=plt.subplots()
        st.subheader("Year-Wise Investments")
        ax.plot(year_wise.index,year_wise.values)
        print(year_wise)
        st.pyplot(fig)

    # Similar investers

 

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup_name')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup_name')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup_name'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total',str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg',str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups',num_startups)

    # Month On Month Graph

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    # plt.xticks()

    st.pyplot(fig3)


def Startup_Analysis(startup):
    temp_df=df[df['invester_name'].str.contains(startup)]

    st.title(startup)
    



    #  most recent five investments

    most_recent=temp_df.head()[[ 'Date', 'invester_name', 'subvertical',
       'city', 'investment_type', 'amount','year']]
    st.subheader('MOst Recent five Investments')
    st.dataframe(most_recent)



    # Biggest Investments
    big_series = temp_df.groupby('startup_name')['amount'].sum().sort_values(ascending=False).head()

    col1,col2=st.columns(2)
    with col1:
        st.subheader('Biggest Investments')
        st.dataframe(big_series)
            
       
    
    with col2:
        fig,ax=plt.subplots()
        st.subheader('Biggest Investments')
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)




    #industry_vertical/Sectorwise Investments

    col3,col4=st.columns(2)

    with col3:

        secter_wise=temp_df.groupby('industry_vertical').sum()['amount'].sort_values(ascending=False)
        st.subheader('secter_wise Investments')
        st.dataframe(secter_wise)
            
       
    
    with col4:
        fig,ax=plt.subplots()
        st.subheader("secter_wise Investments")
        ax.pie(secter_wise.values,labels=secter_wise.index,autopct="%0.01f%%")
        st.pyplot(fig)
        

    # investment_type

    col5,col6=st.columns(2)

    with col5:

        secter_wise=temp_df.groupby('investment_type').sum()['amount'].sort_values(ascending=False)
        st.subheader('Investment_type ')
        st.dataframe(secter_wise)
            
       
    
    with col6:
        fig,ax=plt.subplots()
        st.subheader("Investment Type")

        ax.pie(secter_wise.values,labels=secter_wise.index,autopct="%0.01f%%")
        st.pyplot(fig)        

    # City-wise Investments

    col7,col8=st.columns(2)

    city_wise=temp_df.groupby('city')['amount'].sum().sort_values(ascending=False)

    with col7:
        st.subheader("city-Wise Investments")
        st.dataframe(city_wise)

    with col8:
        fig,ax=plt.subplots()
        st.subheader("city-Wise Investments")
        ax.bar(city_wise.index,city_wise.values)
        # print(year_wise)
        st.pyplot(fig)


    # Years-wise Investments

    col7,col8=st.columns(2)

    year_wise=temp_df.groupby('year')['amount'].sum().sort_values(ascending=False)

    with col7:
        st.subheader("Year-Wise Investments")
        st.dataframe(year_wise)

    with col8:
        fig,ax=plt.subplots()
        st.subheader("Year-Wise Investments")
        ax.plot(year_wise.index,year_wise.values)
        print(year_wise)
        st.pyplot(fig)

    # Similar investers



st.sidebar.title("Startup Funding Analysis")


option=st.sidebar.selectbox('select one',['Overall Analysis','Startup Analysis','Invester Analysis'])

if option=='Overall Analysis':
    load_overall_analysis()
    

elif option=='Startup Analysis':
    startup=st.sidebar.selectbox('Start_ups',startup_name)
    
    butten1=st.sidebar.button("Find Startup Analysis ")
    if butten1:
        Startup_Analysis(startup)
else:
    selected_invester=st.sidebar.selectbox('Investers',Investers)

    butten2=st.sidebar.button("Find Investers Analysis ")
    if butten2:

        details_invester(selected_invester)
    
    # st.title("Invester Analysis")

