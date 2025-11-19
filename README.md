# 📊 Data Analyst Roadmap Plugin

A comprehensive Claude Code plugin for mastering **Data Analysis** from beginner to advanced level. Built on the official [roadmap.sh/data-analyst](https://roadmap.sh/data-analyst) specification.

## ✨ Features

### 🎯 7 Specialist Agents
1. **Foundations & Fundamentals** - Excel, Google Sheets, Data Collection
2. **SQL & Databases** - SQL Mastery, Database Design, Query Optimization
3. **Statistics & Analysis** - Statistical Methods, Hypothesis Testing, Probability
4. **Visualization & BI** - Power BI, Tableau, Dashboard Design, Data Storytelling
5. **Python & R Programming** - Programming, Pandas, NumPy, Data Manipulation
6. **Advanced Analytics** - Predictive Modeling, Regression, Machine Learning, Data Mining
7. **Career Development** - Communication, Leadership, Portfolio Building, Job Search

### 💡 20 Comprehensive Skills
- **Foundations** (3): Excel, Google Sheets, Data Collection
- **Databases/SQL** (3): SQL Basics, Advanced SQL, Database Design
- **Statistics** (3): Descriptive, Inferential, Probability
- **Visualization** (3): Power BI, Tableau, Data Visualization
- **Programming** (3): Python, Pandas/NumPy, R
- **Advanced** (3): Regression, Predictive Modeling, Data Mining
- **Career** (2): Career Development, Communication Skills

### 📚 4 Interactive Commands
- `/learn` - Personalized learning paths (Beginner → Advanced)
- `/explore` - Discover all 7 specialist agents
- `/progress` - Track learning progress and get recommendations
- `/projects` - Real-world hands-on projects (12 projects, all levels)

### ⚡ Intelligent Automation
- Progress tracking and milestones
- Daily engagement reminders
- Weekly learning reviews
- Project completion validation
- Career guidance integration
- Skill badge system

## 📦 Installation

### Easy Installation (Single Command)

```bash
# Load from local directory
plugin add ./custom-plugin-data-analyst

# Or use marketplace (when available)
plugin add data-analyst-roadmap
```

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/pluginagentmarketplace/custom-plugin-data-analyst.git
cd custom-plugin-data-analyst
```

2. In Claude Code:
```
plugin add ./custom-plugin-data-analyst
```

## 🚀 Quick Start

### 1. Initialize Your Learning Path
```
/learn
```
Choose your experience level (Beginner/Intermediate/Advanced) and get a personalized roadmap.

### 2. Explore Specialists
```
/explore
```
Browse all 7 agents and find your area of focus.

### 3. Track Your Progress
```
/progress
```
See what you've learned, identify gaps, and get recommendations.

### 4. Find Projects
```
/projects
```
Discover 12 hands-on projects matching your skill level.

## 📚 Learning Paths

### Beginner Path (6 months)
```
Month 1-2: Excel Fundamentals + Google Sheets
Month 2-3: SQL Basics + Data Collection
Month 3-4: Descriptive Statistics
Month 4-5: Power BI Fundamentals + Python Basics
Month 5-6: First Portfolio Project + Career Setup
```

**Entry Salary**: $40K-$65K
**Skills**: 5-8 completed
**Projects**: 1-2 completed

### Intermediate Path (12 months)
```
Months 1-3: SQL Advanced + Database Design
Months 4-5: Inferential Statistics + Probability
Months 6-7: Python/Pandas Deep Dive
Months 8-9: Tableau/Power BI Advanced
Months 10-11: Regression Analysis + Projects
Month 12: Portfolio + Job Search
```

**Entry Salary**: $65K-$90K
**Skills**: 12-15 completed
**Projects**: 4-6 completed

### Advanced Path (18+ months)
```
Months 1-3: Regression Analysis Mastery
Months 4-6: Predictive Modeling
Months 7-9: Data Mining + Pattern Discovery
Months 10-12: Advanced Dashboard Design
Months 13-15: Specialization (Deep SQL, Advanced Stats, etc.)
Months 16-18: Leadership + Strategic Analytics
```

**Entry Salary**: $90K-$140K+
**Skills**: 18-20 completed
**Projects**: 10+ completed

## 📊 Plugin Statistics

| Component | Count | Status |
|-----------|-------|--------|
| **Agents** | 7 | ✅ Complete |
| **Skills** | 20 | ✅ Complete |
| **Commands** | 4 | ✅ Complete |
| **Projects** | 12 | ✅ Complete |
| **Code Examples** | 100+ | ✅ Included |
| **Learning Hours** | 500+ | ✅ Content |
| **Resources** | 50+ | ✅ Linked |
| **Hooks** | 10 | ✅ Automation |

## 🎯 Core Components

### Agents (Specialized Expertise)
Each agent provides deep expertise in a specific area with:
- Detailed learning phases
- Real-world projects
- Career progression guidance
- Best practices and tools
- Next steps for advancement

### Skills (SKILL.md Format)
Each skill file includes:
- YAML frontmatter metadata
- Quick start examples
- 5 key concepts with code
- Tools and resources
- Best practices checklist
- Real-world applications
- Next steps pathway

### Commands (User Interactions)
Four powerful commands for:
- Personalized learning path generation
- Agent discovery and exploration
- Progress tracking and insights
- Project-based learning

### Hooks (Automation)
10 intelligent hooks for:
- Progress saving and tracking
- Daily reminders and motivation
- Weekly reviews and adjustments
- Project validation
- Badge and milestone celebrations

## 🌟 Unique Features

### Production-Quality Content
- 100+ code examples in Excel, SQL, Python, R
- Real-world datasets and scenarios
- Industry-standard tools and frameworks
- Current best practices (2024)

### Complete Career Integration
- Salary expectations by level
- Job market analysis
- Interview preparation
- Portfolio building guidance
- Networking strategies

### Hands-On Learning
- 12 progressively challenging projects
- Real datasets from actual sources
- Portfolio-building opportunities
- Mentor guidance available

### Intelligent Automation
- Smart progress tracking
- Personalized recommendations
- Motivation and engagement hooks
- Career path guidance
- Skill badge system

## 📖 File Structure

```
custom-plugin-data-analyst/
├── .claude-plugin/
│   └── plugin.json ............................ Official manifest
│
├── agents/ (7 files)
│   ├── 01-foundations-specialist.md
│   ├── 02-sql-databases-expert.md
│   ├── 03-statistics-specialist.md
│   ├── 04-visualization-architect.md
│   ├── 05-programming-expert.md
│   ├── 06-advanced-analytics-specialist.md
│   └── 07-career-coach.md
│
├── commands/ (4 files)
│   ├── learn.md
│   ├── explore.md
│   ├── progress.md
│   └── projects.md
│
├── skills/ (7 categories, 20 skills)
│   ├── foundations/ (3 skills)
│   ├── databases-sql/ (3 skills)
│   ├── statistics/ (3 skills)
│   ├── visualization/ (3 skills)
│   ├── programming/ (3 skills)
│   ├── advanced/ (3 skills)
│   └── career/ (2 skills)
│
├── hooks/
│   └── hooks.json ............................ Automation config
│
├── README.md ................................ This file
├── LEARNING-PATH.md ......................... Detailed roadmap
├── GETTING-STARTED.md ....................... Quick setup guide
├── LICENSE .................................. MIT License
└── .gitignore

Total: 40+ files, 15,000+ lines of content
```

## 🎓 Learning Approach

### Progressive Complexity
1. **Master Fundamentals First** - Excel, data basics
2. **Build Core Skills** - SQL, Statistics
3. **Add Programming** - Python/R
4. **Advanced Techniques** - Modeling, Mining
5. **Career Growth** - Communication, Leadership

### Hands-On Projects
Every skill connects to practical projects:
- Data cleaning exercises
- Analysis projects
- Dashboard creation
- Statistical studies
- Predictive models
- Portfolio pieces

### Real-World Tools
Learn actual industry tools:
- Excel (pivot tables, formulas, automation)
- SQL (across multiple databases)
- Power BI (Microsoft standard)
- Tableau (popular visualization)
- Python (pandas, scikit-learn, matplotlib)
- R (dplyr, ggplot2, statistical functions)

## 💼 Career Outcomes

### After 6 Months (Beginner)
✅ Excel proficiency
✅ SQL query basics
✅ Statistical foundations
✅ Dashboard creation
✅ First portfolio project
**Target Role**: Junior Data Analyst
**Salary**: $40K-$65K

### After 12 Months (Intermediate)
✅ Advanced SQL & optimization
✅ Statistical testing mastery
✅ Programming proficiency
✅ Advanced visualizations
✅ 4-6 portfolio projects
**Target Role**: Data Analyst
**Salary**: $65K-$90K

### After 18-24 Months (Advanced)
✅ Predictive modeling
✅ Machine learning basics
✅ Advanced analytics
✅ Business intelligence
✅ 10+ portfolio projects
✅ Leadership skills
**Target Role**: Senior Data Analyst / Analytics Manager
**Salary**: $90K-$140K+

## 🔧 Technical Requirements

- Claude Code 0.5.0 or higher
- Modern web browser
- 500MB free disk space
- No additional software needed (guides provided for each tool)

## 🤝 Support & Community

- **Built-in Help**: Use `/help` command
- **Documentation**: Comprehensive guides included
- **Community**: Share learning progress and projects
- **Feedback**: Report issues and suggest improvements

## 📝 Version History

**v1.0.0** (November 2024)
- 🎉 Complete plugin release
- 7 specialist agents
- 20 comprehensive skills
- 4 interactive commands
- 12 hands-on projects
- 10 automation hooks
- 100+ code examples

## 📄 License

MIT License - Free to use, modify, and distribute
See LICENSE file for details

## 🙏 Acknowledgments

Based on the official [roadmap.sh/data-analyst](https://roadmap.sh/data-analyst) specification
Created with modern best practices for developer education

## 🚀 Next Steps

1. **Install the plugin**:
   ```bash
   plugin add ./custom-plugin-data-analyst
   ```

2. **Start learning**:
   ```
   /learn
   ```

3. **Track progress**:
   ```
   /progress
   ```

4. **Build projects**:
   ```
   /projects
   ```

---

**Ready to become a Data Analyst?** Start your journey with `/learn` command! 🎯📊
