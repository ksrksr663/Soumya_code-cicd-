FROM python
# using python image from docker hub
WORKDIR /soumyacode
# creating and changing folder in docker image
COPY automate.py /soumyacode/
CMD [ "python" , "automate.py" ]
# run the python code while creating container