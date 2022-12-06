import streamlit as st

def main():
    st.title("Division Calculator")

    with st.form(key='form1'):
        dividend = st.text_input("Dividend")
        divisor = st.text_input("Divisor")

        submit_button = st.form_submit_button(label='Divide')

    if submit_button:
        try:
            if float(divisor) != 0:
                result = round(float(dividend)/float(divisor),4)
                st.success( "{} &#247; {} = {}".format(dividend, divisor, result))
            else:
                st.error("Divisor should NOT be zero (0)")    
        except:        
            st.error("Dividend and Divisor must be numbers")

if __name__ == '__main__':
    main()