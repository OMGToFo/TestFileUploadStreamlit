import streamlit as st

import pandas as pd

#Process Pictures

from PIL import Image

#@st.cache
#def load_image(image_file):
#	img = Image.open(image_file)
#	return img


st.title = "File Upload"


menu = ["Home", "CSV","Excel","Documentfiles", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
	st.subheader("Home")
	image_file = st.file_uploader("Upload Images", type=["png","jpg", "jpeg"])
	#if image_file is not None:
		#st.write(type(image_file))
		#st.write(dir(image_file))	
		#st.image(load_image(image_file))
	
elif choice == "CSV":
	st.subheader("Dataset")
	data_file = st.file_uploader("Upload CSV", type=["csv"])
	if data_file is not None:
		st.write(type(data_file))
		file_details = {"filename":data_file.name,
		"filesize":data_file.size}
		st.write(file_details)
		df = pd.read_csv(data_file)
		st.dataframe(df)


elif choice == "Excel":
	st.subheader("Excel-Dataset")
	data_file = st.file_uploader("Upload Excel", type=["xlsx","xls", "xlsm"])
	if data_file is not None:
		st.write(type(data_file))
		file_details = {"filename":data_file.name,
		"filesize":data_file.size}
		st.write(file_details)
		df = pd.read_excel(data_file)
		st.dataframe(df)
		dataAuswahl = pd.read_excel(data_file,
                    usecols='H:I')
		st.dataframe(dataAuswahl)	
		dataAuswahl.set_index('Kurvenscheitel' ,inplace=True)		
		st.line_chart(dataAuswahl)




	
elif choice == "DocumentFiles":
	st.subheader("DocumentFiles")
	
else:
	st.subheader("About")
	
	
