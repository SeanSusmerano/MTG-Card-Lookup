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

## Usage

## Roadmap

### Phase 1: Core Functionality
- [x] Find an API to search MTG cards with
- [x] Go through text list of MTG cards and filter out profitable cards
- [x] Implement a way to show progress on how many cards on the list has been searched

### Phase 2: Data Storage Improvements
- [ ] Add Google Docs integration to replace the text files
- [ ] Add prompts to properly populate the correct Google Sheets
- [ ] Create a Google Sheets Template

### Phase 3: Refinement
- [ ] Implement a way to check recently checked cards to see if a card can be skipped in search
- [ ] Optimize API request batching to improve speed
- [ ] Handle API rate limiting more gracefully

## Contact
Sean Susmerano - - susmeranosean@gmail.com
Project Link: https://github.com/SeanSusmerano/MTG-Card-Lookup
