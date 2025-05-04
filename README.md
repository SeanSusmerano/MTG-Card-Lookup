# MTG-Card-Lookup

## Table of Contents
- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing]
- [License]
- [Contact](#contact)
- [Acknowledgements]

## About the Project
This project processes a list of bulk Magic: The Gathering cards, filtering out those worth over $1. 
The goal is to sell high-value cards individually and sell the remaining bulk to local shops.

## Built With
- [Python](https://www.python.org/)
- [requests](https://requests.readthedocs.io/en/latest/) for handling HTTP requests
- [Google Sheets API](https://developers.google.com/sheets) for Google Sheets integration

## Getting Started

### Prerequisites

### Installation

1. Clone the repo
   
   git clone https://github.com/SeanSusmerano/MTG-Card-Lookup.git

3. Get a Google API credentials

   Go to https://console.cloud.google.com
   - Navigate to Google Sheets API: https://console.cloud.google.com
      - Create a new project and select it to make it the active project you are working on.
      - Click the "burger" button on the upper left hand corner and click "APIs & Services". Then click "Enabled APIs & Services".
      - Then click "+ ENABLE APIS AND SERVICES" and then search for "Google Sheets API". Select it and "Enable" it.
      - Click "Create Credentials".
        - Leave "Select an API" as "Google Sheets API and select "Application Data".
        - Create a name and then click "Create and Continue".
        - For "Select a role", search for "Editor" and pick "Editor".
        - Click "Done".
     - Click the "Credentials" tab, under "Service Accounts", click the email that was just created.
        - We will also need that email address, so copy the email address and save it for later.
     - Go to the "Keys" tab and click "Add Key".
        - Select "JSON" and click "Create" so we can download the private key.
     - Rename it to "credentials.json" and drop it into your repo, replacing the pre-existing empty "credentials.json"

4. Setup your Google Sheets

   Go to https://docs.google.com/spreadsheets/d/101dVi5c5JYgGuusMnPslOSN0Fzl39o_7BNSGz7ausqI/edit?usp=sharing
   - Download the template and upload it to your own personal Google Drive.
   - Once you have your own copy of the template, open it, and click "Share" on the upper right hand corner.
      - You will need that email from earlier and paste it into "Add people, groups, and calendar events".
      - Make sure to give it "Editor" privilages, and then click "Send".
   - You will need the link to the document when running this project.

## Usage

## Roadmap

### Phase 1: Core Functionality
- [x] Find an API to search MTG cards with
- [x] Go through text list of MTG cards and filter out profitable cards
- [x] Implement a way to show progress on how many cards on the list has been searched

### Phase 2: Data Storage Improvements
- [x] Add Google Docs integration to replace the text files
- [x] Add prompts to properly populate the correct Google Sheets
- [x] Create a Google Sheets Template

### Phase 3: Refinement
- [ ] Implement a way to check recently checked cards to see if a card can be skipped in search
- [ ] Optimize API request batching to improve speed
- [ ] Handle API rate limiting more gracefully
- [ ] Improve Documentation

## Contact
Sean Susmerano - - susmeranosean@gmail.com
Project Link: https://github.com/SeanSusmerano/MTG-Card-Lookup
