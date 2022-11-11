# linkedin-email-verifier
The script uses Google's search engine to look for public Linkedin profiles based on the domain name.
It then converts them to the specific email format for that company. This can be useful when you need emails for a big list of domains.
It does require you to have knowledge of the email for the company is using, so first a site like phonebook.cz or hunter.io can be used to find the correct format.

1. (Install python3 first) then use: pip3 install google-api-python-client

2. Go to https://console.cloud.google.com/, create an google account and go to the credentials tab.

3. Click on create credentials and select API keys.

4. copy the API key to dev_key=<add API key> in verifyemails.py.

5. Go to https://programmablesearchengine.google.com/controlpanel/all and click on create your own search engine.

6. In our case we're just looking for search results from linkedin.com so you can add this url to the "search specific site" option and leave the rest on default.

7. You should now have a link that looks like this: https://cse.google.com/cse?cx=<your cse id>

8. Copy your cse id to cse_id=<add cse id> in verifyemails.py.

9. Create workemails.txt in the same directory as verifyemails.py and add the domains you want to search emails for.

10. Now if you use the script with: python3 verifyemails.py, it should throw an error saying something like:
"Custom Search API has not been used in project x before or it is disabled. Enable it by visiting: <url> ..."

11. Go the URL (redirects to your project) and click enable API.

12. Now you can use the API to search for results on linkedin.com (If it still throws the same error then wait about 5 minutes and try again).

13. Results are saved to workemailsoutput.txt and formatting options are saved to savedoptions.txt.
