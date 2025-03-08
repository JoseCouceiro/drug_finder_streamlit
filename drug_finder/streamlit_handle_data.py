import requests
import csv
import io
import streamlit as st

class HandleData(): 

    def __init__(self):
        st.markdown(
                        """
                        <style>
                        div.stDownloadButton > button:first-child {
                            background-color: #008CBA; /* Button background color */
                            color: white; /* Text color */
                            border-radius: 10px; /* Rounded corners */
                            padding: 10px 20px;
                            font-size: 16px;
                            border: none;
                            cursor: pointer;
                        }
                        
                        div.stDownloadButton > button:first-child:hover {
                            background-color: #E04E1F; /* Darker shade on hover */
                        }
                        </style>
                        """,
                        unsafe_allow_html=True
                    )

    def download_as_pdf(self, response):
        __name = response['nombre']
        __docs = response['docs']
        
        try:           
            for __el in __docs:    
                if __el["tipo"] == 2:
                    __url = response['docs'][__docs.index(__el)]['url']
            response = requests.get(__url)
            pdf_bytes = response.content
            

            st.download_button(
                                label="Download drug prospect as PDF",
                                data=pdf_bytes,
                                file_name=f"{__name}.pdf",
                                mime="application/pdf"
                                )  
        except:
            st.write('Prospect not available in database')
            pass
        
    def download_as_csv(self, query, response):    
        csv_buffer = io.StringIO()
        csv_writer = csv.writer(csv_buffer)  
        self.__i = 0
        for __,__dic in response.items():
            for __med in __dic['resultados']:
                self.__i += 1
                csv_writer.writerow((f"{self.__i}", f"{__med['nombre']}"))
        csv_string = csv_buffer.getvalue()
        csv_buffer.close()
        st.download_button(
                            label= "Download list of medicines as csv",
                            data=csv_string,
                            file_name=f"{query}.csv",
                            mime="text/csv"
                            )
    









