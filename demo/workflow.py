def process_docs(text):
    return {
        "Department" : "Finance", 
        'Task' : "Invoice Processing", 
        "Summary": text[:180] + "....", 
        "Status": "Ready for AI review",
    }