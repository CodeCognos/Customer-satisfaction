from zenml.client import Client

#client = Client()

#stacks = client.list_stacks()
#for stack in stacks:
    #print(f"Stack Name: {stack.name}, Stack ID: {stack.id}")


#from zenml import Client

#stack_id = "077a922c-0696-40bd-9a27-1885c90b4a21"
#client = Client()
#activated_stack = client.activate_stack(stack_id)

#if activated_stack is not None:
    #experiment_tracker = getattr(activated_stack, 'experiment_tracker', None)
    #if experiment_tracker:
        # Use experiment_tracker as needed
       # print("Experiment tracker found!")
    #else:
        #print("Experiment tracker attribute not found.")
#else:
    #print("Failed to activate the stack.")

print(Client().active_stack.experiment_tracker.get_tracking_uri())

#mlflow ui  --backend-store-uri "file:C:/Users/Mehta/AppData/Roaming/zenml/local_stores/b2e36199-7f4c-43d2-950c-fd87c732cf06/mlruns"


#mlflow ui  --backend-store-uri "file:C:/Users/Mehta/AppData/Roaming/zenml/local_stores/b2e36199-7f4c-43d2-950c-fd87c732cf06/mlflow_model_deployer_step/output/1969eb70-21e4-4fe2-b8c8-09af95fb2b6f"
mlflow ui  --backend-store-uri "file:C:/Users/Mehta/AppData/Roaming/zenml/local_stores/b2e36199-7f4c-43d2-950c-fd87c732cf06\mlruns"