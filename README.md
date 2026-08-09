# 🎮 Steam Market Intelligence Platform

> An end-to-end data analytics project that collects Steam game data, transforms and stores it in a normalized MySQL database, and uses Power BI to generate interactive market insights.

🚧 **Project Status: In Development**

---

## 📌 Overview

The Steam Market Intelligence Platform is an end-to-end data analytics project built to collect, organize, and analyze Steam game marketplace data.

The project is designed around a scalable data pipeline that extracts game information from Steam, processes the collected data, stores it in a normalized MySQL database, and prepares it for interactive analysis and visualization using Power BI.

The current development focuses on building a scalable scraping pipeline capable of collecting data from multiple Steam pages and populating the relational database efficiently.

---

## 🎯 Business Problem

Steam contains a large amount of game-related information, including:

- Game details
- Prices
- Reviews
- Genres
- Developers
- Publishers
- Platform availability

However, this information is presented primarily for individual users rather than structured business analysis.

This project aims to transform this raw marketplace information into a structured analytical dataset that can be used to understand patterns in the Steam gaming ecosystem.

---

## 🎯 Project Objectives

- Build a scalable Steam data extraction pipeline
- Collect game metadata from multiple pages
- Clean and transform scraped data
- Design a normalized relational database
- Separate entities into dimension, fact, bridge, and repository tables
- Populate the database with large-scale scraped data
- Connect the database to Power BI
- Build interactive dashboards
- Identify trends and patterns across games, genres, publishers, developers, reviews, prices, and platforms

---

# 🔄 Project Architecture

```text
                         ┌─────────────────┐
                         │      Steam      │
                         │   Store Pages   │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Python Scraper  │
                         │  BeautifulSoup  │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Data Parsing &  │
                         │ Transformation  │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     MySQL       │
                         │ Relational DB   │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        Dimension Tables      Fact Tables       Bridge Tables
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │    Power BI     │
                         │    Dashboard    │
                         └─────────────────┘
                                  │
                                  ▼
                         Business Insights
```

# 🛠️ Technology Stack

### 📥 Data Collection

- Python
- BeautifulSoup
- Requests

### 🧹 Data Processing

- Python
- Custom Data Transformation Pipeline

### 🗄️ Database

- MySQL
- SQL
- Relational Database Design

### 📊 Business Intelligence

- Microsoft Power BI

### ⚙️ Development

- Git
- GitHub
- VS Code

---

# 📊 Data Being Collected

The project currently works with game-level information such as:

- Steam App ID
- Game Name
- Release Date
- Price
- Review Summary
- Publisher
- Developer
- Genre
- Platform Availability

Additional market metrics are being incorporated as the project evolves.

---

# 🗄️ Database Design

The project uses a normalized MySQL database designed to minimize data duplication and maintain clear relationships between entities.

The database includes multiple types of tables:

### Dimension Tables

Store descriptive information about entities such as:

- Games
- Publishers
- Developers
- Genres
- Platforms

### Fact Tables

Store measurable game and market-related metrics.

### Bridge Tables

Handle many-to-many relationships between entities where required.

### Repository Tables

Support the storage and management of scraped data within the data pipeline.

The schema is designed to support scalable data collection as the scraper expands from individual pages to multiple Steam pages.

---

# 📈 Power BI Analytics

Power BI will serve as the primary analytical and visualization layer of this project.

The MySQL database will provide structured data to Power BI for interactive analysis and reporting.

### Planned Analysis Areas

#### 🎮 Game Analysis

- Game distribution
- Price analysis
- Review analysis
- Platform availability

#### 🏷️ Genre Analysis

- Game distribution by genre
- Genre-level pricing
- Review performance across genres

#### 🏢 Publisher & Developer Analysis

- Publisher game portfolios
- Developer game portfolios
- Review performance

#### 💰 Pricing Analysis

- Free vs. paid games
- Price distribution
- Pricing patterns across categories

#### ⭐ Review Analysis

- Review sentiment distribution
- Relationship between reviews and other game attributes

> 🚧 **Power BI dashboard is currently under development.**

---

# 🔎 SQL in This Project

SQL is primarily used as the **database layer** of the project.

It is currently used for:

- Database schema creation
- Dimension and fact table creation
- Bridge table creation
- Repository table creation
- Constraints
- Indexes
- Table relationships

The primary analytical and visualization layer of this project is **Power BI**.

A separate SQL case study will use the same Steam dataset to demonstrate advanced SQL-based business analysis.

---

# 🚧 Current Development Stage

The project is currently in the **scaling stage**.

### ✅ Completed

- [x] Project architecture
- [x] Steam scraper
- [x] HTML parsing
- [x] Data transformation
- [x] MySQL database connection
- [x] Relational database schema
- [x] Dimension tables
- [x] Fact tables
- [x] Bridge tables
- [x] Repository tables
- [x] Database relationships

### 🔄 Currently Working On

- [ ] Scaling scraper to multiple Steam pages
- [ ] Populating the database with larger datasets
- [ ] Validating relationships across populated tables
- [ ] Preparing the database for Power BI
- [ ] Building Power BI dashboard
- [ ] Developing analytical KPIs
- [ ] Generating business insights

---

# 🔮 Future Improvements

- Automated scheduled scraping
- Historical data snapshots
- Price trend analysis
- Review trend analysis
- Genre-level market analysis
- Publisher and developer benchmarking
- Automated data refresh
- Advanced Power BI reporting
- Predictive market analysis

---

# 📂 Project Structure

```text
steam-market-intelligence/
│
├── .vscode/
│
├── assets/
│
├── config/
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── database/
│
├── docs/
│
├── logs/
│
├── models/
│
├── notebooks/
│
├── powerbi/
│
├── scraper/
│
├── sql/
│   ├── queries/
│   └── schema/
│
├── tests/
│
├── transform/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

# 🧪 Development Approach

The project is being developed incrementally through the following phases:

### Phase 1 - Architecture
Design the project structure and relational database schema, including dimensions, facts, bridge tables, and repository tables.

### Phase 2 - Data Collection
Build and validate the Steam scraper, request handling, and HTML parsing pipeline.

### Phase 3 - Data Transformation
Clean, standardize, validate, and transform the extracted Steam data into structured records suitable for database storage.

### Phase 4 - Database Integration
Populate the normalized MySQL database and maintain relationships between games, publishers, developers, genres, platforms, and market metrics.

### Phase 5 - Scaling
Expand the scraper from individual pages to multiple Steam pages and populate the database with a larger dataset.

### Phase 6 - Business Intelligence
Connect the MySQL database to Power BI and develop interactive dashboards for exploring Steam marketplace data.

### Phase 7 - Analytics
Analyze the collected dataset and generate data-driven business insights through Power BI.

---

# 📊 Project Goals

The final platform aims to answer business-oriented questions such as:

- How are games distributed across different genres?
- How does pricing vary across different game categories?
- Which publishers and developers have the largest game portfolios?
- How are games distributed across Windows, macOS, and Linux?
- What is the distribution of review sentiment?
- What patterns can be identified between game attributes and market metrics?
- Which genres show differences in pricing and review performance?
- What insights can be derived from the overall Steam game marketplace?

The final conclusions and insights will be based on the actual collected dataset and Power BI analysis rather than assumptions or predefined results.

---

# 🔗 Related SQL Case Study

A separate **Steam Market SQL Case Study** will use the dataset generated by this project to demonstrate analytical SQL skills through business-oriented questions.

The case study will focus on techniques such as:

- JOINs
- Aggregations
- GROUP BY
- CASE statements
- Common Table Expressions (CTEs)
- Subqueries
- Window Functions
- Date Functions

The SQL case study will focus specifically on **SQL-based business analysis**, while this project focuses on the complete data pipeline, MySQL database design, and **Power BI-based analytics**.

This separation allows the two projects to demonstrate different aspects of the same data platform:

**Steam Market Intelligence**

> Data Collection → Transformation → MySQL → Power BI → Business Insights

**Steam Market SQL Case Study**

> MySQL Dataset → SQL Analysis → Business Questions → Insights

> 🚧 **Steam Market SQL Case Study — Coming Soon**

---

# 👨‍💻 Author

## Mohd. Sami

Aspiring Data Analyst focused on **SQL, Python, Power BI, MySQL, and data-driven problem solving**, with additional interests in Data Science and AI/ML.

- GitHub: [Sami21234](https://github.com/Sami21234)
- LinkedIn: [Mohd. Sami](https://www.linkedin.com/in/mohd-sami-dev)

---

⭐ **If you find this project interesting, consider giving it a star!**