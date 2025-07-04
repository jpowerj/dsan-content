import datetime, getpass, ipylab, ipywidgets, IPython.display, pytz, time
jfe = ipylab.JupyterFrontEnd()
button, output = ipywidgets.Button(description="Submit HW1"), ipywidgets.Output()
IPython.display.display(button, output)
def generate_timestamp(datetime_obj):
    return str(datetime_obj).split(".")[0].replace(" ","_").replace(":","").replace("-","")
def on_button_clicked(b):
    with output: print("Saving notebook...")
    jfe.commands.execute('docmanager:save')
    time.sleep(0.2)
    output.clear_output()
    with output: print("Submitting...")
    cur_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
    cur_ts = cur_time.strftime('%X %p, %x')
    cur_ts_short = generate_timestamp(cur_time)
    !/srv/submit.sh HW1 {str(cur_ts)}
    time.sleep(0.2)
    output.clear_output()
    with output: print(f"HW1 submitted at {str(cur_ts)} [Check feedback folder]")
    netid = getpass.getuser().replace("jupyter-","")
    time.sleep(1)
    jfe.commands.execute('filebrowser:open-path', args={'path': f'HW1/feedback/{cur_ts_short}_{netid}.txt'})
button.on_click(on_button_clicked)
