# Chat2Note

`chat2note` is a tool that converts conversations with `ChatGPT` into notes, making it easier to save and review important discussions.

## Installation

### Prerequisites
- Operating System: `Windows` or `MacOS`
- `Chrome` browser installed
- `Python 3.8+`
- Accessible `ChatGPT` website

### Installation Steps

1. Clone the project to your local machine:
   ```bash
   git clone https://github.com/CosmicResearchCenter/chat2note.git
   ```

2. Navigate to the project directory and install the dependencies:

   ```bash
   pip install .
   ```

   

##  Usage Guide

### Set Environment Variables

Before running the tool, configure the following environment variables based on your operating system:

#### Windows
```bash
$env:BASE_URL="Your OPENAI API base URL"
$env:API_KEY="Your OPENAI API key"
$env:MODEL="Model name"
```
#### MacOS
```bash
export BASE_URL="Your OPENAI API base URL"
export API_KEY="Your OPENAI API key"
export MODEL="Model name"
```
### Running the Tool

Use the share link of your ChatGPT conversation with the following command:
```bash
chat2note -u https://chatgpt.com/share/xxxxx
```
Success Message

Once the tool runs successfully, you should see the following output:
```bash
-------------------------------------------------start-------------------------------------------------
Retrieving user conversation history.
Successfully retrieved user conversation history.
Retrieving AI conversation history.
Successfully retrieved AI conversation history.
Parsing conversation history
Conversation history parsing completed
Generating note ...
Note generation complete
Generating file name ...
The file name is generated, and the file name is xxxxx
Note has been saved to xxxx.md file
--------------------------------------------------end--------------------------------------------------
```

## Future Plans

- [ ] 
  Support for more models
- [ ] Support for scraping content through a web crawler