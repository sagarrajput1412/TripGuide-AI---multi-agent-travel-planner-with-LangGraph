


user_input = input("Enter travel request: ") 

response = run_travel_agent(
    user_input = user_input,
    thread_id = "test_user"         # just for testing purpose
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])
