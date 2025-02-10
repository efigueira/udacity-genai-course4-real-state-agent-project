# Project: Personalized Real Estate Agent

# Project Overview

## Project Introduction
Imagine you're a talented developer at **"Future Homes Realty"**, a forward-thinking real estate company. In an industry where personalization is key to customer satisfaction, your company wants to revolutionize how clients interact with real estate listings. The goal is to create a personalized experience for each buyer, making the property search process more engaging and tailored to individual preferences.

---

## The Challenge
Your task is to develop an innovative application named **"HomeMatch"**. This application leverages large language models (LLMs) and vector databases to transform standard real estate listings into personalized narratives that resonate with potential buyers' unique preferences and needs.

---

## Core Components of "HomeMatch"

### **1. Understanding Buyer Preferences**
- Buyers will input their requirements and preferences, such as:
  - Location
  - Property type
  - Budget
  - Amenities
  - Lifestyle choices
- The application uses **LLMs** to interpret these inputs in natural language, understanding nuanced requests beyond basic filters.

### **2. Integrating with a Vector Database**
- Connect "HomeMatch" with a **vector database** where all available property listings are stored.
- Utilize **vector embeddings** to match properties with buyer preferences, focusing on:
  - Neighborhood vibes
  - Architectural styles
  - Proximity to specific amenities

### **3. Personalized Listing Description Generation**
- For each matched listing:
  - Use an **LLM** to rewrite the description in a way that highlights aspects most relevant to the buyer’s preferences.
  - Ensure personalization emphasizes characteristics appealing to the buyer without altering factual information about the property.

### **4. Listing Presentation**
- Output the personalized listing(s) as a **text description** of the property.

---

# Instructions

## Project Instructions
To create the **"HomeMatch"** application, follow these steps. Build the application in a Jupyter Notebook or Python file(s). A workspace is provided on the next page with several dependencies already installed. It is good practice to create a GitHub repository for development. Submit a zip file containing the application and supporting documentation. Your project will be assessed against this [rubric](https://review.udacity.com/#!/rubrics/5403/view).

---

### **Step 1: Setting Up the Python Application**
- **Initialize a Python Project**: 
  - Create a new Python project, set up a virtual environment, and install necessary packages such as:
    - LangChain
    - A suitable LLM library (e.g., OpenAI's GPT)
    - A vector database package (e.g., ChromaDB or LanceDB)
  - If you don't wish to start from scratch, starter files are available in the workspace.

---

### **Step 2: Generating Real Estate Listings**
- **Generate Real Estate Listings**:
  - Use a Large Language Model (LLM) to create at least 10 property listings by designing prompts for the LLM. Example:
    ```
    Neighborhood: Green Oaks
    Price: $800,000
    Bedrooms: 3
    Bathrooms: 2
    House Size: 2,000 sqft

    Description: Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.

    Neighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.
    ```
  - Use these listings to populate the database for testing and development.

---

### **Step 3: Storing Listings in a Vector Database**
- **Vector Database Setup**:
  - Initialize and configure a vector database (e.g., ChromaDB) to store property listings.
- **Generate and Store Embeddings**:
  - Convert the LLM-generated listings into vector embeddings that capture their semantic content and store them in the database.

---

### **Step 4: Building the User Preference Interface**
- **Collect Buyer Preferences**:
  - Gather buyer preferences interactively or through hard-coded questions/answers. Example:
    ```python
    questions = [
        "How big do you want your house to be?",
        "What are 3 most important things for you in choosing this property?",
        "Which amenities would you like?",
        "Which transportation options are important to you?",
        "How urban do you want your neighborhood to be?",
    ]
    answers = [
        "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
        "A quiet neighborhood, good local schools, and convenient shopping options.",
        "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
        "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
        "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
    ]
    ```
- **Preference Parsing**:
  - Implement logic to interpret and structure buyer preferences for querying the vector database.

---

### **Step 5: Searching Based on Preferences**
- **Semantic Search**:
  - Use the structured buyer preferences to perform a semantic search on the vector database.
- **Listing Retrieval Logic**:
  - Fine-tune the retrieval algorithm to select the most relevant listings based on semantic similarity.

---

### **Step 6: Personalizing Listing Descriptions**
- **LLM Augmentation**:
  - Use the LLM to rewrite property descriptions for the matched listings, emphasizing aspects most relevant to the buyer's preferences.
- **Maintain Factual Integrity**:
  - Ensure the augmented descriptions highlight appealing features without altering factual information.

---

### **Step 7: Deliverables and Testing**
- **Testing**:
  - Test the "HomeMatch" application against various "buyer preferences" to ensure it meets all rubric requirements.
- **Code Structure**:
  - Write the application code in a Jupyter notebook or a standalone Python program. Ensure it is well-commented and logically structured.
- **Example Outputs**:
  - Include outputs demonstrating how buyer preferences are processed and how listings are personalized.

---

### **Step 8: Project Submission**
- **Generated Listings**:
  - Include a file named `listings` containing your generated property listings.
- **Project Documentation**:
  - Add a README file explaining functionality, prerequisites, and how to run the code.
- **Submit Code**:
  - Submit the Jupyter Notebook or Python program in a zip file on the project submission page.

---

### **Stand-Out Suggestion**
To make your project stand out:
- Add images and implement multi-modal search using **CLIP** to match images with text-based real estate descriptions in your "HomeMatch" application.

---

# Environments

## Project Environment
For this project, you will need:
- **Python**
- A **vector database** (e.g., ChromaDB or LanceDB)
- A **Large Language Model** (e.g., OpenAI API GPT-3.5 is recommended)

Follow the instructions on the **Get a Vocareum OpenAI API Key** page to obtain your API key. Consider using tools such as **LangChain** or **GPT Function calling** to simplify development.

You can complete the project in the provided workspace or build the project locally.

---

## Local Machine Instructions
If you choose to build the project locally:
1. **Initialize a virtual environment** for the project.
2. Consider managing your code with a **GitHub repository**.
3. Install the following locally:
   - Python
   - Jupyter Notebook or VS Code
4. Use `pip` to install the dependencies. A `requirements.txt` file is available in the workspace below for download.

---

## Workspace Instructions
- Use the provided **workspace** to create your application.
- The workspace will **auto-save your progress**.
- Download a copy of your project code or sign in to GitHub to commit your code to a remote repository.
- You can also submit your project directly through the workspace.

---

# Project: Personalized Real Estate Agent

## Synthetic Data Generation

| **Criteria**                              | **Submission Requirements**                                                                                                     |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Generating Real Estate Listings with an LLM | The submission must demonstrate using a Large Language Model (LLM) to generate at least 10 diverse and realistic real estate listings containing facts about the real estate. |

---

## Semantic Search

| **Criteria**                                     | **Submission Requirements**                                                                                                     |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Creating a Vector Database and Storing Listings | The project must demonstrate the creation of a vector database and successfully storing real estate listing embeddings within it. The database should effectively store and organize the embeddings generated from the LLM-created listings. |
| Semantic Search of Listings Based on Buyer Preferences | The application must include a functionality where listings are semantically searched based on given buyer preferences. The search should return listings that closely match the input preferences. |

---

## Augmented Response Generation

| **Criteria**                                         | **Submission Requirements**                                                                                                     |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Logic for Searching and Augmenting Listing Descriptions | The project must demonstrate a logical flow where buyer preferences are used to search and then augment the description of real estate listings. The augmentation should personalize the listing without changing factual information. |
| Use of LLM for Generating Personalized Descriptions  | The submission must utilize an LLM to generate personalized descriptions for the real estate listings based on buyer preferences. The descriptions should be unique, appealing, and tailored to the preferences provided. |

# Suggestions to Make Your Project Stand Out

For a project that truly stands out, consider integrating **CLIP** to enable multimodal search capabilities. This advanced feature would allow the application to search real estate listings through textual descriptions and images associated with each property. By doing so, the application can align visual elements of a property (like style, layout, and surroundings) with the textual buyer preferences.

---

## Implementation Overview

### **Image Embeddings**
- Generate embeddings for real estate images using **CLIP**, which can then be stored in the vector database alongside text embeddings.

### **Multimodal Search Logic**
- Develop a search algorithm that considers both text and image embeddings to find listings that best match the buyer's preferences, including visual aspects.
