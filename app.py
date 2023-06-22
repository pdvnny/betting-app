# Parker Dunn (pgdunn@bu.edu)
# The "main" script for running my streamlit app

# UPDATES
# - 6/21/2023: Started the application and used a simple graph demo
#			   to get a streamlit app running

from src.demo import demo  	# For demo only!
import time					# For demo only!

import streamlit as st

# ===============================================================
#     --------- ??? --------
# ===============================================================

def setup_page():
	st.title("Betting Dashboard")
	st.subheader("Enter a new bet to track or request information about your bet history.")
	st.text_input("Enter your username: ", key="username")
	st.text_input("Enter your password: ", key='pw')

def run_app():
	return None


# ===============================================================
#     --------- demo web app --------
# ===============================================================

def run_app_demo():
	# The username stuff doesn't actually do much here.
	# It is just a way to 

	# if "username" not assigned yet...
	# if "last_username" not in st.session_state:
		# st.session_state.last_username = ""

	# if run is typed in the username box, then do something
	if st.session_state.username == 'run':

		# Just wanted to add this for fun
		st.spinner()
		with st.spinner(text="Grabbing the demo figure..."):
			time.sleep(1)
			figure = demo()
			st.pyplot(figure)
			# st.balloons()   # This just a balloons graphic??

	else:

		st.markdown("Please type `run` in the username box to run the demo code.")

# ===============================================================
#     --------- main --------
# ===============================================================

if __name__ == '__main__':
	setup_page()

	run_app_demo()
