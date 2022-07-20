# The data we need to retrieve.
# 1. Total number of votes cast
# 2. Complete list of candidates who recieved votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote.

# add our dependencies
import csv
import os
# assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initialize a total vote counter
total_votes = 0
# candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # read the header row
    headers = next(file_reader)
    # print each row in the CSV file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1
        # get the candidate name from each row
        candidate_name = row[2]
        # if the candidate does not match any existing candidate, add to the candidate list
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # and begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# save the results to our text file
with open(file_to_save, "w") as txt_file:
    # after opening the file print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # after printing the final vote count to the terminal save the final vote count to the text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        #  save the candidate results to our text file
        txt_file.write(candidate_results)
        # determine winning vote count, winning percentage, and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)