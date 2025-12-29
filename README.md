# P.I.T.A - Pantry Inventory Tracking Application

## URL of the DEMO video

URL: 

## Project Overview

### Description:

P.I.T.A (Pantry Inventory Tracking Application) is a web-based application designed to help users manage their food inventory, reduce food waste, and discover recipes based on available ingredients. The application allows users to track items in their pantry, freezer, and refrigerator, monitor expiration dates, and generate recipe suggestions using AI.


### Technologies Used

- **Backend**: 
  - Python with Flask framework
  - CS50 SQL library for database operations
  - SQLite database for data storage
  - Flask-Session for session management
  - OpenAI API for AI-powered recipe generation
  - SMTP for email functionality

- **Frontend**:
  - HTML/CSS for structure and styling
  - JavaScript for dynamic interactions
  - Responsive design for mobile and desktop compatibility (***not entirely finished***)

## Project Structure

The project follows a clear separation between backend and frontend components:

### Backend (`/backend`)

- **`app.py`**: The main Flask application file containing all route definitions, database connections, and application logic.
- **`ai/`**: Contains AI-related functionality.
  - **`ai_llm_management.py`**: Manages interactions with the OpenAI API for recipe generation.
- **`mail/`**: Contains email functionality.
  - **`mail_management.py`**: Handles sending contact form emails.
- **`login/`**: Contains authentication-related functionality.
- **`pantry.sqlite`**: SQLite database storing user information, pantry items, and saved recipes.

### Frontend (`/frontend`)

- **`templates/`**: Contains HTML templates for all pages.
  - **`layout.html`**: Base template that all other templates extend.
  - **`home.html`**: Landing page introducing the application.
  - **`discover.html`**: Information page about the application's features.
  - **`login.html`**: User authentication page (login and registration).
  - **`dashboard.html`**: Main user interface for managing pantry items.
  - **`item_definition.html`**: Form for adding or editing pantry items.
  - **`assistant.html`**: AI recipe generation interface.
  - **`recipies.html`**: Saved recipes display page.
  - **`contact.html`**: Contact form page.

- **`static/`**: Contains static assets.
  - **`css/`**: Stylesheet files for all pages.
  - **`scripts/`**: JavaScript files for dynamic functionality.
  - **`icon.png`**, **`icon.ico`**, **`welcome_img.png`**: Images used throughout the application.

## Key Features

### User Authentication
- Secure registration and login system
- Password hashing for security
- Session management for user state

### Pantry Management
- Add, edit, and delete food items
- Categorize items by type (vegetables, fruits, meat, etc.)
- Track quantities, units, and expiration dates
- Specify storage location (pantry, freezer, refrigerator)

### AI-Powered Recipe Generation
- Generate recipe suggestions based on available pantry items
- Identify additional ingredients needed for recipes
- Provide nutritional information and cooking instructions
- Save favorite recipes for future reference

### Responsive Design
- Mobile-friendly interface (***Still needs to be finished***)
- Consistent styling across all pages
- Intuitive navigation and user experience

## Installation and Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with the following variables:
   ```
   PATH_TO_DB=pantry.sqlite
   SESSION_SK=your_secret_key
   OPEN_AI_KEY=your_openai_api_key
   EMAIL_SENDER=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   ```
6. Initialize the database: `flask init-db` (if applicable)
7. Run the application: `flask run`

## Usage Instructions

1. **Registration/Login**: Create an account or log in to access the dashboard.
2. **Dashboard**: View and manage your pantry inventory.
3. **Add Items**: Click "Add Element" to add new items to your pantry.
4. **Edit/Delete Items**: Use the action buttons to modify or remove items.
5. **Generate Recipes**: Navigate to "Generate Recipes" to get AI-powered recipe suggestions.
6. **Save Recipes**: Save interesting recipes for future reference.
7. **View Saved Recipes**: Access your saved recipes from the "My Recipes" page.

## Design Choices and Considerations

### Architecture
I chose a Flask-based architecture for its simplicity and flexibility. The separation between backend and frontend components allows for easier maintenance and potential future expansion. The SQLite database was selected for its lightweight nature and ease of setup, making it perfect for a personal project of this scale. I also used the `cs50` module for db management because of its simplicity of use.

### User Interface
The UI design prioritizes simplicity and usability. I implemented a consistent color scheme and layout across all pages to provide a cohesive user experience. The responsive design ensures the application works well on both desktop and mobile devices, allowing users to access their pantry information from anywhere.

### Security
Security was a key consideration in the development process. The application implements:
- Password hashing to protect user credentials
- Session management with secure cookies
- CSRF protection (***Commented in the current version of the code since I did not put it into production yet***)
- Input validation to prevent injection attacks
- Content Security Policy headers

### AI Integration
The integration with OpenAI's API allows for intelligent recipe generation based on available ingredients. I designed the prompt carefully to ensure the AI generates practical, realistic recipes that prioritize using existing pantry items while suggesting minimal additional purchases. This approach aligns with the application's goal of reducing food waste and unnecessary shopping.

### Future Enhancements
While the current version provides a solid foundation, several enhancements could be considered for future iterations:
- Barcode scanning for easier item entry
- Meal planning calendar
- Grocery list generation
- Expiration date notifications
- Social sharing of recipes
- Integration with online grocery services

### AI Usage - in accordance with CS50 requirements
This project was designed and implemented entirely by me, in full accordance with CS50’s policy on the appropriate use of AI tools. 

I used ChatGPT as a support resource for discussing design ideas, clarifying concepts, and debugging specific issues, in a manner comparable to consulting documentation or seeking high-level guidance. 

The entire project was developed inside JetBrain - PyCharm IDE, so I also used Junie (built-in AI assistant) to assist with extending and refining CSS styling to improve visual consistency across the application.

At all times, I retained full understanding and control over the codebase. All architectural choices, core logic, and implementation decisions were my own, and no AI-generated content was used without being reviewed, understood, and, where necessary, adapted by me. The AI tools were used strictly as aids to learning and refinement, not to generate solutions beyond my own comprehension or to replace my own work.

## Conclusion

P.I.T.A represents a practical solution to common kitchen management challenges that I myself have been faced daily. By combining inventory tracking with AI-powered recipe suggestions, the application will hopefully help users make the most of their available ingredients, reduce food waste, and discover new culinary possibilities. The project demonstrates the effective use of web technologies and AI integration to create a useful, user-friendly application.

