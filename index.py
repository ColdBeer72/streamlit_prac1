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
    # st.dataframe(iris)
    gestiona_filtros(iris)

def gestiona_filtros(df):
    especies_unicas = df["species"].unique()
    st.text(especies_unicas)
    especies_seleccionadas = st.multiselect(label="Especie de Flor", options=especies_unicas,)
    df2 = df[
        df["species"].isin(especies_seleccionadas)
    ]

    # SEPAL LENGTH
    sepal_length_min = df2["sepal_length"].min()
    sepal_length_max = df2["sepal_length"].max()

    ## SEPAL LENGTH MIN
    form_sepal_length_min = st.slider(label="Sepal Length MIN",
                                      min_value=sepal_length_min,
                                      max_value=sepal_length_max,
                                      value=sepal_length_min,
                                      step=0.1)
    st.text(f"Sepal Length MIN: {form_sepal_length_min}")

    ## SEPAL LENGTH MAX
    form_sepal_length_max = st.slider(label="Sepal Length MAX",
                                      min_value=form_sepal_length_min,
                                      max_value=sepal_length_max,
                                      value=sepal_length_max,
                                      step=0.1)
    st.text(f"Sepal Length MAX: {form_sepal_length_max}")

    df3 = df2[
        (df2["sepal_length"] >= form_sepal_length_min) &
        (df2["sepal_length"] <= form_sepal_length_max)
    ]

    # SEPAL WIDTH
    sepal_width_min = df3["sepal_width"].min()
    sepal_width_max = df3["sepal_width"].max()

    ## SEPAL WIDTH MIN
    form_sepal_width_min = st.slider(label="Sepal Width MIN",
                                     min_value=sepal_width_min,
                                     max_value=sepal_width_max,
                                     value=sepal_width_min,
                                     step=0.1)
    st.text(f"Sepal Width MIN: {form_sepal_width_min}")

    ## SEPAL WIDTH MAX
    form_sepal_width_max = st.slider(label="Sepal Width MAX",
                                     min_value=form_sepal_width_min,
                                     max_value=sepal_width_max,
                                     value=sepal_width_max,
                                     step=0.1)
    st.text(f"Sepal Width MAX: {form_sepal_width_max}")

    df4 = df3[
        (df3["sepal_width"] >= form_sepal_width_min) &
        (df3["sepal_width"] <= form_sepal_width_max)
    ]

    # PETAL LENGTH
    petal_length_min = df4["petal_length"].min()
    petal_length_max = df4["petal_length"].max()

    ## PETAL LENGTH MIN
    form_petal_length_min = st.slider(label="Petal Length MIN",
                                      min_value=petal_length_min,
                                      max_value=petal_length_max,
                                      value=petal_length_min,
                                      step=0.1)
    st.text(f"Petal Length MIN: {form_petal_length_min}")

    ## PETAL LENGTH MAX
    form_petal_length_max = st.slider(label="Petal Length MAX",
                                      min_value=form_petal_length_min,
                                      max_value=petal_length_max,
                                      value=petal_length_max,
                                      step=0.1)
    st.text(f"Petal Length MAX: {form_petal_length_max}")

    df5 = df4[
        (df4["petal_length"] >= form_petal_length_min) &
        (df4["petal_length"] <= form_petal_length_max)
    ]

    # PETAL WIDTH
    petal_width_min = df5["petal_width"].min()
    petal_width_max = df5["petal_width"].max()

    ## PETAL WIDTH MIN
    form_petal_width_min = st.slider(label="Petal Width MIN",
                                     min_value=petal_width_min,
                                     max_value=petal_width_max,
                                     value=petal_width_min,
                                     step=0.1)
    st.text(f"Petal Width MIN: {form_petal_width_min}")

    ## PETAL WIDTH MAX
    form_petal_width_max = st.slider(label="Petal Width MAX",
                                     min_value=form_petal_width_min,
                                     max_value=petal_width_max,
                                     value=petal_width_max,
                                     step=0.1)
    st.text(f"Petal Width MAX: {form_petal_width_max}")

    df6 = df5[
        (df5["petal_width"] >= form_petal_width_min) &
        (df5["petal_width"] <= form_petal_width_max)
    ]
    st.dataframe(df6)

if __name__ == "__main__": 
    index()