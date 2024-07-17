import streamlit as st
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import modules.page_config as pc

def index():
    json = pc.get_page_config_default()
    st.set_page_config(**json)
    st.title(":blue[Practicando] con Streamlit en :orange[Hack a Boss]")
    st.header("Bootcamp de Data Science e Inteligencia Artificial")
    st.subheader("Autor: Manuel Tornos")
    iris = sns.load_dataset('iris')
    # st.subheader("DataFrame Original")
    # st.dataframe(iris)
    # st.subheader("Gráfica Completa")
    # grafica(iris)
    df_res = gestiona_filtros(iris)
    st.subheader("Gráfica FILTRADA")
    grafica(df_res)
    
def grafica(df):
    # Define las variables para el gráfico
    variable_x = st.selectbox("Variable X", df.columns)  # Permite al usuario seleccionar la variable X
    variable_y = st.selectbox("Variable Y", df.columns)  # Permite al usuario seleccionar la variable Y
    tipo_grafico = st.selectbox("Tipo de gráfico", ["Violinplot", "Lineplot", "Barplot"])  # Permite al usuario seleccionar el tipo de gráfico
 
    # Crea la figura de Matplotlib
    fig, ax = plt.subplots()

    # Crea el gráfico según el tipo seleccionado
    if tipo_grafico == "Violinplot":
        sns.violinplot(
            x=variable_x,
            y=variable_y,
            data=df,
            ax=ax
        )
    elif tipo_grafico == "Lineplot":
        sns.lineplot(
            x=variable_x,
            y=variable_y,
            data=df,
            ax=ax
        )
    elif tipo_grafico == "Barplot":
        sns.barplot(
            x=variable_x,
            y=variable_y,
            data=df,
            ax=ax
        )

    # Personaliza el título, etiquetas y leyenda del gráfico
    ax.set_title(f"{tipo_grafico} de {variable_x} vs {variable_y}")
    ax.set_xlabel(variable_x)
    ax.set_ylabel(variable_y)

    # Muestra el gráfico en Streamlit
    st.pyplot(fig)


    sns.set_style()
    sns.violinplot(data=df,
                   x="species",
                   y="sepal_length")
    plt.title("Distribución del largo del sépalo por especie")
    plt.xlabel("Especie")
    plt.ylabel("Largo del sépalo (cm)")
    plt.show()

def gestiona_filtros(df):
    especies_unicas = df["species"].unique()
    st.subheader("Filtros")
    especies_seleccionadas = st.multiselect(label="TIPO DE ESPECIE",
                                            options=especies_unicas,
                                            default=especies_unicas)
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
            
            valmin = df2[tcons].min()
            valmax = df2[tcons].max()

            texto = f"{tcons}".upper()
            valmin, valmax = st.slider(label=texto,
                                      min_value=valmin,
                                      max_value=valmax,
                                      value=(valmin, valmax),
                                      step=0.1)
            st.text(f"{texto}: {valmin}, {valmax}")

            df2 = df2[
                (df2[tcons] >= valmin) &
                (df2[tcons] <= valmax)]
            
    st.subheader("DATAFRAME FILTRADO")
    st.dataframe(df2)
    return df2

if __name__ == "__main__": 
    index()