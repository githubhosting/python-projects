import streamlit as st
import os
import base64
import requests
from selenium import webdriver
import bs4


def main():
    url = "https://github.com/githubhosting/Noterep/issues/new"
    issue_body = {"id": "issue_body"}
    allData = {
        'login': "githubhosting",
        'password': "Mr14061974",
    }

    site_session = requests.Session()
    _ = site_session.get('https://github.com/login')  # This is just to get the initial
    # cookie in the session
    siteRequest = site_session.post('https://github.com/login', data=allData)
    print(siteRequest.content, end='\n\n')

    st.title("GitLinker")
    st.write("This is a simple app to create a link to a file that are uploaded to issue tab in github")
    file_path = "demo.png"
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "text/plain")}
        issue_body = {"id": "issue_body"}
        response = requests.post(url, data=issue_body, files=files)
        st.write(response.text)


if __name__ == "__main__":
    main()
