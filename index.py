import streamlit as st
import pandas as pd
import requests
import seaborn as sns
import modules.page_config as pc

def index():
    json = pc.get_page_config_default()
    st.set_page_config(**json)
    st.title(":blue[Practicando] con Streamlit en :orange[Hack a Boss]")
    st.header("Bootcamp de Data Science e Inteligencia Artificial")
    st.subheader("Autor: Manuel Tornos")
    iris = sns.load_dataset('iris')
    st.dataframe(iris)
    gestiona_filtros(iris)

def gestiona_filtros(df):
    especies_unicas = df["species"].unique()
    st.text(especies_unicas)
    especies_seleccionadas = st.multiselect(label="Especie de Flor",
                                            options=especies_unicas,)
    df2 = df[
        df["species"].isin(especies_seleccionadas)
    ]

    tvars1 = ["sepal", "petal"]
    tvars2 = ["length", "width"]
    tdict = dict()

    for tvariable1 in tvars1:
        for tvariable2 in tvars2:
            tcons = f"{tvariable1}_{tvariable2}"
            tdict[tcons] = ""

            texto = f"{tcons}".upper()
            valmin, valmax = st.slider(label=texto,
                                      min_value=df2[tcons].min(),
                                      max_value=df2[tcons].max(),
                                      value=(df2[tcons].min(), df2[tcons].max()),
                                      step=0.1)
            st.text(f"{texto}: {valmin}, {valmax}")

            df2 = df2[
                (df2[tcons] >= valmin) &
                (df2[tcons] <= valmax)]
            
    st.dataframe(df2)

if __name__ == "__main__": 
    index()