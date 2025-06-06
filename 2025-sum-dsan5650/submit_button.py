import datetime, getpass, ipylab, ipywidgets, IPython.display, pytz, time
from redis import Redis
from rq import Queue
jfe = ipylab.JupyterFrontEnd()
button, output = ipywidgets.Button(description="Submit HW1"), ipywidgets.Output()
IPython.display.display(button, output)
def generate_timestamp(datetime_obj):
    return str(datetime_obj).split(".")[0].replace(" ","_").replace(":","").replace("-","")
def get_elapsed(t0):
    elapsed_delta = datetime.datetime.now() - t0
    return elapsed_delta.seconds
def on_button_clicked(b):
    with output: print("Saving notebook...")
    jfe.commands.execute('docmanager:save')
    time.sleep(0.2)
    cur_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
    cur_ts = generate_timestamp(cur_time)
    output.clear_output()
    with output: print(f"Submitting assignment (submission timestamp {cur_ts})...")
    username = getpass.getuser()
    netid = username.replace("jupyter-","")
    q = Queue(connection=Redis())
    enqueue_time = datetime.datetime.now()
    jag_job = q.enqueue("jagtask.grade_user", "DSAN5650", "HW1", username, cur_ts)
    time.sleep(0.2)
    while jag_job.is_queued:
        output.clear_output()
        elapsed = get_elapsed(enqueue_time)
        with output: print(f"Submission in queue (elapsed time: {str(elapsed)})...")
        time.sleep(0.5)
    while jag_job.is_started:
        output.clear_output()
        elapsed = get_elapsed(enqueue_time)
        with output: print(f"Notebook execution started (elapsed time: {str(elapsed)})...")
        time.sleep(1)
    if jag_job.is_finished:
        output.clear_output()
        elapsed = get_elapsed(enqueue_time)
        result_fpath = f'HW1/feedback/{netid}_HW1_{cur_ts}.html'
        with output: print(f"Grading complete! Opening {result_fpath}...")
        jfe.commands.execute('docmanager:open-browser-tab', args={'path': result_fpath})
    else:
        output.clear_output()
        with output: print(f"Submission error (please retry, and if the issue persists, email dsan5650-staff@georgetown.edu)")
button.on_click(on_button_clicked)
