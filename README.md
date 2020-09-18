# Twitter-Trending-Streaming
Using Twitter API to get tweet data and using spark stream to track '#' trending hashtags. Using Chart.js to visualization of trending hashtags.

If you want to run this repo. follow these steps.
 
- First you can clone it and then install all requirements.

    ```
    git clone https://github.com/shivamgupta7/Twitter-Trending-Streaming.git

    # using pip you can install all the requirement.

    cd Twitter-Trending-Streaming

    pip3 install -r requirements.txt
    ```
- After install all the requirements you can run ```twitterConnectivity.py``` file 
    ``` 
    python twitterConnectivity.py
    ```
- Then run ```spark-streaming.py```
    ```
    python spark-streaming.py
    ```
- At the last you can run ```app.py``` for visulaization on your localhost:5000
    ```
    python app.py
    ```
- Open your browser and run ```localhost:5000```