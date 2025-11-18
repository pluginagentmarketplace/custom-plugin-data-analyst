---
name: "Google Sheets"
description: "Learn cloud-based spreadsheet collaboration, automation with Apps Scripts, and API integration for real-time data analysis"
category: "Foundations"
level: "Beginner-Intermediate"
duration: "3-5 weeks"
---

# Google Sheets

## Quick Start

Google Sheets enables real-time team collaboration and automation. Within your first week, you'll share sheets, use QUERY functions, and create automated reports. By week three, you'll build Apps Scripts to pull data from APIs and trigger automated workflows.

**First Task (20 minutes):**
1. Go to sheets.google.com and create a new spreadsheet
2. Share it with a teammate for editing
3. Add sample data and apply conditional formatting
4. Use QUERY function to filter and summarize data
5. Create a simple chart

## Key Concepts

### 1. Cloud Collaboration
**What it is:** Real-time simultaneous editing with version history and comment capabilities.

**Features:**
- **Share & Permissions:** Set editor, viewer, or commenter access
- **Version History:** Restore previous versions (View → Version history)
- **Comments & Tasks:** @mention colleagues, assign tasks
- **Simultaneous Editing:** See cursor positions of team members live

**When to use:** Team projects, client deliverables, dashboards requiring real-time updates.

### 2. QUERY Function
**What it is:** SQL-like syntax to filter, sort, and aggregate data without pivot tables.

**Example:**
```
=QUERY(A:D, "SELECT A, SUM(D) WHERE B='North' GROUP BY A")
Filters data where column B = 'North'
Sums column D values and groups by column A
```

**When to use:** Creating dynamic reports, filtering by user input, building dashboards from raw data.

### 3. Apps Scripts & Automation
**What it is:** JavaScript-based automation to extend Google Sheets with custom functions and workflows.

**Example:**
```javascript
function updateReport() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getRange("A1:D100").getValues();
  var today = new Date();
  sheet.getRange("F1").setValue("Last updated: " + today);
}
```

**When to use:** Auto-sending reports, pulling data from APIs, creating custom functions, scheduled updates.

### 4. API Integration
**What it is:** Connect external data sources to Google Sheets for real-time imports.

**Common integrations:**
```
=IMPORTJSON(url, "/path/to/field")    # Import JSON data
=IMPORTHTML(url, "table", index)       # Scrape HTML tables
=GOOGLEFINANCE("GOOGL")                # Stock prices
=IMPORTDATA(url)                       # CSV or TSV files
```

**Example workflow:**
```
Source: REST API returning JSON sales data
Target: Google Sheet that auto-updates hourly
Use: Apps Script with UrlFetchApp.fetch()
```

### 5. Add-ons & Extensions
**What it is:** Third-party tools that extend Google Sheets functionality.

**Popular Add-ons:**
- **Data Studio:** Create interactive dashboards
- **Supermetrics:** Pull marketing data (Google Ads, Facebook)
- **Mailmodo:** Collect form responses
- **Lucidchart:** Embed diagrams
- **Pivot Table:** Enhanced pivot functionality

## Tools and Resources

**Google Sheets Platform:**
- sheets.google.com (free with Google account)
- Mobile apps (Android/iOS)
- Offline editing support

**Developer Resources:**
- Google Sheets API Documentation: https://developers.google.com/sheets
- Apps Script Documentation: https://developers.google.com/apps-script
- Sample Scripts: GitHub google/apps-script-samples

**Useful Add-ons:**
- Data Studio: Free dashboard builder
- Supermetrics: Social media & marketing data
- Polymorphic: Dynamic form responses

## Best Practices

1. **Set Clear Permissions:** Define who can edit vs. view to prevent accidental changes
2. **Use Naming Conventions:** Name sheets and ranges descriptively (e.g., "RawData", "Dashboard")
3. **Create Data Validation:** Restrict entries to predefined lists for consistency
4. **Separate Layers:** Keep raw data, working sheets, and dashboards in different tabs
5. **Document Scripts:** Add comments in Apps Scripts explaining logic
6. **Test Before Automation:** Manually verify QUERY and formula logic before automating
7. **Monitor API Quotas:** Track API usage to avoid hitting limits
8. **Archive Old Versions:** Keep team folders organized with clear naming conventions

## Next Steps

1. **Week 1-2:** Master QUERY, IMPORTRANGE, and basic filtering
2. **Week 2-3:** Build a collaborative dashboard with charts
3. **Week 3-4:** Create first Apps Script for API data ingestion
4. **Week 4-5:** Set up automated reports with scheduled triggers
5. **After:** Move to Data Studio for advanced dashboard design
6. **Progression:** Google Sheets → Python/Pandas for complex transformations
