import streamlit as st

def main():
    st.title("Division Calculator")

    with st.form(key='form1'):
        dividend = st.text_input("Dividend")
        divisor = st.text_input("Divisor")

        submit_button = st.form_submit_button(label='Divide')

    if submit_button:
        result = float(dividend)/float(divisor)
        st.success( "{} divided by {} = {}".format(dividend, divisor, result))


if __name__ == '__main__':
    main()