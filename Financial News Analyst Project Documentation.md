# Financial News Analyst Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Backend (Django)](#backend-django)
   - [API Endpoints](#api-endpoints)
   - [Data Processing](#data-processing)
4. [Frontend (React)](#frontend-react)
   - [User Interface](#user-interface)
   - [State Management](#state-management)
5. [API Usage](#api-usage)
6. [Deployment](#deployment)
7. [Examples of Generated Outcomes](#examples-of-generated-outcomes)
8. [Troubleshooting](#troubleshooting)

## Project Overview

The Financial News Analyst is a web application designed to provide users with quick, AI-generated analyses of company earnings reports. By inputting a company name, quarter, and year, users can receive a summarized report of the company's financial performance for that period.

### Key Features:
- User-friendly interface for inputting company and time period data
- AI-powered analysis of financial reports
- Presentation of key financial metrics and insights
- Links to source materials for further reading

## System Architecture

The project follows a client-server architecture:

1. **Frontend**: React-based single-page application (SPA)
2. **Backend**: Django REST API
3. **AI Service**: OpenAI GPT model for text generation
4. **External Data Source**: Tavily API for retrieving financial data

## Backend (Django)

The backend is built with Django and Django REST Framework, providing a robust and scalable server-side solution.

### API Endpoints

- `POST /api/chat/`
  - Accepts JSON payload with `company`, `quarter`, and `year`
  - Returns AI-generated analysis of the company's financial report

### Data Processing

1. The backend receives the user input.
2. It constructs a query string for the Tavily API.
3. Financial data is fetched from Tavily.
4. The data is processed and sent to the OpenAI GPT model.
5. The AI-generated analysis is returned to the frontend.

## Frontend (React)

The frontend is a React application, providing a responsive and interactive user interface.

### User Interface

- Input fields for company name, quarter, and year
- "Get earning report" button to trigger the analysis
- Results display area with formatted text output

### State Management

- React hooks (`useState`) are used for local state management
- Axios is used for API calls to the backend

## API Usage

To use the Financial News Analyst API:

1. Send a POST request to `/api/chat/`
2. Include a JSON payload with the following structure:

```json
{
  "company": "NVIDIA",
  "quarter": "3",
  "year": "2024"
}
```

3. The API will respond with a JSON object containing the analysis:

```json
{
  "analysis": "Based on the given data, NVIDIA has announced impressive financial results for the third quarter of fiscal 2024. [...]"
}
```


## Examples of Generated Outcomes

Example 1: NVIDIA Q3 2024

```
Based on the given data, NVIDIA has announced impressive financial results for the third quarter of fiscal 2024. The company reported record-breaking revenue of $18.12 billion, representing a 206% increase compared to the same period last year and a 34% rise from the previous quarter. NVIDIA's strong growth is attributed to the transition from general-purpose to accelerated computing and generative AI.

Key Highlights:
- Data Center revenue reached a record $14.51 billion.
- GAAP earnings per diluted share surged to $3.71.
- Colette Kress, NVIDIA's executive vice president and CFO, provided insights into the company's financial health and future prospects.

[...]
```

Example 2: Apple Q1 2024

```
Apple has reported strong financial results for the first quarter of fiscal 2024. The company achieved record quarterly revenue of $119.6 billion, showing a 2% increase year-over-year. This performance exceeded analyst expectations and demonstrated Apple's resilience in a challenging economic environment.

Key Highlights:
- iPhone revenue reached $69.7 billion, growing by 6% year-over-year.
- Services revenue set a new all-time record of $23.1 billion, up 11% from the previous year.
- Apple's installed base of active devices surpassed 2.2 billion.

[...]
```

## Troubleshooting

1. **API Connection Issues**: 
   - Ensure the backend server is running and accessible
   - Check for any CORS issues in the browser console

2. **No Data Returned**: 
   - Verify the input data (company name, quarter, year) is correct
   - Check the Tavily API connection and quota

3. **Formatting Issues**: 
   - Ensure the CSS for pre-formatted text is correctly applied
   - Check for any unexpected characters in the API response

For further assistance, please open an issue in the project's GitHub repository.
