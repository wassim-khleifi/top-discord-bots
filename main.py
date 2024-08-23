import os, requests
from dotenv import load_dotenv

load_dotenv()

## top.gg request
def topgg_request():
	api_key = os.getenv('TOPGG_API_KEY')
	url = "https://top.gg/api/bots?sort=monthlyPoints&limit=10"
	headers = {
	"Authorization": api_key
	}
	request = requests.get(url,headers=headers)
	bots = request.json()['results']
	return bots

## create tables
def create_table(bots):
	content = "| Bot name        | Monthly votes           | Invite link  |\n| ------------- |:-------------:| -----:|\n"
	for bot in bots:
		content += f"| {bot['username']}      | {bot['points']} | [Click me]({bot['invite']}) |\n"
	return content

## Get readme old content
def get_previous_content(readme_content):
	readme_previous_content = ""
	for content in readme_content[:16]:
		readme_previous_content += content
	return readme_previous_content

## Edit readme
def update_readme(content):
	readme_file = open('README.md', 'r')
	readme_content = readme_file.readlines()
	readme_previous_content = get_previous_content(readme_content)

	readme_file = open('README.md', 'w')
	final_content = readme_previous_content + "\n" + content
	readme_file.write(final_content)
	readme_file.close()
	print("Successfully updated readme with the new statics.")

## Main function
def main():
	bots = topgg_request()
	table = create_table(bots)
	update_readme(table)

if __name__ == "__main__":
	main()