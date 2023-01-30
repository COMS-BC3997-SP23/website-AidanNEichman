# AidanNEichman.github.io
COMS BC 3997 Project Website

# Project: "Optimizing Player Rest in Basketball using Machine Learning"

# Introduction (Problem Idenitification & Target Audience): 
The basketball industry is highly competitive and the performance of individual players plays a crucial role in the success of a team. One important aspect of player performance is proper rest and recovery, especially for the big contract players who are relied upon to deliver on the field. The problem this project addresses is optimizing rest schedules for these players to ensure they perform at their best and reduce the risk of injury.

The target audience for this project is the coaching and management staff of basketball teams, specifically those teams with high-priced and high-performing players. These individuals are responsible for making decisions about player schedules and need accurate and reliable information to do so.

This project will benefit the target audience by providing them with data-driven recommendations for rest schedules that maximize player performance and reduce the risk of injury. By considering factors such as previous workload, injury history, and performance data, the project will give teams a competitive edge and help ensure their star players remain healthy and effective throughout the season. In addition, by reducing the risk of injury, teams can protect their investments in high-priced players and minimize the financial and performance costs of injured players. Ultimately, this project will help teams win more games and achieve greater success.

# Methodology:
- Collect and clean player performance data from various sources such as NBA
  statistics and player tracking data.
- Develop a model using C++ and Python to analyze the performance data and
  predict optimal rest periods for each player.
- This model will be based on Machine learning algorithms like Random Forest,
  XGBoost, Neural Network and will be implemented using libraries like
scikit-learn, Tensorflow.
- Evaluate the performance of the model using metrics such as accuracy and
  precision.
- Use the model to predict rest periods for players on a given schedule of
opponents.

# Expected Outcomes and Measurables:
Because mindful rest schedules are a newer idea in basketball, there is not a lot of previously-recorded rest schedules through which I can see if my model is on the right track. However, there does exist some data within the past 5-6 years that can be used as a baseline comparison for the model. I am still figuring out how I can test the optimization aspect of the model (which will hoepfully come to me as I work through more strictly defining the model as a whole). Otherwise, I think that success would look like having a model that gather, interacts with, and utilizes all of the different categorical data in the game of basketball.

- Improved performance and reduced injury risk for individual players on the
  team.
- A model that can be used to optimize rest schedules for other teams in the
  league.
- Improved understanding of the factors that affect player performance and the
  role of rest in maintaining peak performance.

# Timeline:

- Data collection and cleaning: 3 weeks
- Model development and debugging: 5 weeks
- Model evaluation and improvement: 2 weeks

# Background Materials/Resources:
For Tangible Statistics:
- https://www.nbastuffer.com/2022-2023-nba-rest-days-stats/ (NBA per team rest day stats)
- https://www.nbastuffer.com/2022-2023-nba-player-stats/ (NBA per player stats)
- https://www.nba.com/stats/players/boxscores-traditional (NBA per game, per player advanced box scores)

For Rest Day Background Research:
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6107769/ (Injury Risk in the NBA)
- https://journals.sagepub.com/doi/pdf/10.1177/23259671221121116 (Condensed Schedule Argument)
- https://repository.ihu.edu.gr/xmlui/bitstream/handle/11544/29991/Georgios%20Papageorgiou%20Dissertation%20Data%20Mining%20in%20Sports.pdf?sequence=1 (Data Mining for Player Performance Predictions)
- https://www.tandfonline.com/doi/epdf/10.1080/24751839.2021.1977066?needAccess=true&role=button (ML in NBA Predictions)
