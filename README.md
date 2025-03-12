# Hostfully API Integration Guideline
 - python3 -m pip install requests
 - python3 -m pip install python-dotenv
  -- optional use can use python instead on python in the above command based on your version installed

# create .env file
 - copy the the string that will be provided for you to .env

# Run each files using the following command
# to get Guest Information and Notes
  - python3 leads.py - this will generate a file called leads.csv and leads.json with all the booking information, along with the guest information and notes

# to get all the Guest information / this is i get from Hostfully Notes after my requests
 - python3 messages.py - this will generate a file called messages.csv and messages.json with all the guest messages, since it's empty i can't be sure, but it's testing environment so that might be the reason.

  - the other files i have created are the integrations for the other endpoints, since i figured you may need them in future.

   - and if you need any help with the integration, please let me know, i will be happy to help you out.