# InstaQuotes - Instagram Quote Image Automation

This project automates the process of fetching quotes, generating images, and uploading them to Instagram using python. It uses the **Pillow** library to generate images, **Imgur** to host images, and **Facebook Graph API** to post the images on Instagram.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Overview](#project-overview)
- [Step-by-Step Guide](#step-by-step-guide)
  - [Step 1: Create an Imgur Account and Obtain App ID](#step-1-create-an-imgur-account-and-obtain-app-id)
  - [Step 2: Create a Facebook Developer Account](#step-2-create-a-facebook-developer-account)
  - [Step 3: Set Up an Instagram Business Account](#step-3-set-up-an-instagram-business-account)
  - [Step 4: Create a Facebook Page](#step-4-create-a-facebook-page)
  - [Step 5: Obtain Facebook Page ID](#step-5-obtain-facebook-page-id)
  - [Step 6: Get Access Tokens](#step-6-get-access-tokens)
  - [Step 7: Automate Image Upload and Posting](#step-7-automate-image-upload-and-posting)
- [License](#license)

## Prerequisites
- Python 3.x
- Pillow library (`pip install pillow`)
- Requests library (`pip install requests`)
- A [Facebook](https://www.facebook.com/) account
- A [Facebook Developer](https://developers.facebook.com/) account
- An [Instagram Business](https://business.instagram.com/) account
- An [Imgur](https://imgur.com/) account

## Project Overview
This project fetches a random quote, generates an image using the Pillow library, uploads the image to Imgur (to obtain a publicly accessible URL), and finally posts the image to Instagram using the Facebook Graph API. There are a few pre-requisite steps needed for the scripts to run. You can use your own methods to automate this (github workflow, linux env, etc.)

## Guide

### Step 1: Create an Imgur Account and Obtain App ID
1. Go to [Imgur](https://imgur.com/register) and create an account.
2. After logging in, navigate to [Imgur API Registration](https://api.imgur.com/oauth2/addclient).
3. Click **Create New Application** and select "OAuth 2 authorization without a callback URL."
4. Fill in the required details and submit.
5. Note your **Client ID** and **Client Secret**.

### Step 2: Create a Facebook Developer Account
1. Visit [Facebook for Developers](https://developers.facebook.com/) and sign in / sign up.
2. Click on **My Apps** and then **Create App**.
3. Select **Business** as the app type, and fill in the details.
4. You will be taken to the app dashboard after creation.

### Step 3: Set Up an Instagram Business Account
1. On Instagram, sign in or create an account.
2. Go to **Settings** > **Account** > **Switch to Professional Account**.
3. Follow the prompts to set up your business account.
4. You will need to link your Instagram account to a Facebook Page (covered in the next step).

### Step 4: Create a Facebook Page
1. Go to the [Create Page](https://www.facebook.com/pages/create) section on Facebook.
2. Choose a category (Business, Brand, etc.) and fill in the necessary details.
3. Once your page is created, go to the **Settings** of your page, find **Linked Accounts**, and connect your Instagram account.

### Step 5: Obtain Facebook Page ID
1. Go to [Facebook Graph Explorer](https://business.facebook.com/latest/settings/instagram_account/), select your instagram account, and note down your ID. This is your page ID.

### Step 6: Get Access Tokens
1. Go to [Facebook Graph Explorer](https://developers.facebook.com/tools/explorer/)
2. In Graph Explorer, select your app from the drop down, User Token and click Get Access Token and select the following permissions:
   - instagram_basic
   - instagram_content_publish
   - pages_show_list
   - pages_read_engagement
   - pages_manage_posts
4. Use the Access Token Debugger to extend the lifespan of your token:
   - Select Tools > Access Token Debugger
   - Paste the token into the debugger and click Debug.
   - Select Extend Access Token to convert it into a long-lived token (valid for 60 days).

### Step 7: Automate Image Upload and Posting
1. Configure Imgure token
   Create an environment variable / github secret with name "IMGUR_CLIENT_ID" and paste your Imgur client ID.
2. Configure Facebook tokens
   Create 2 environment variable / github secret with name "FACEBOOK_PAGE_ID" and "FACEBOOK_ACCESS_TOKEN" and paste the respective values in them.
3. Run or schedule the upload_image.py script for automation.

## License
MIT License
