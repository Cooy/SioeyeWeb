import HTMLTestRunner
import os
import time
def run_with_report(cases,reporttitle,reportdescription,casesname):

    for filename in os.listdir('./'):
        if filename == "report":
            break
    else:
        os.mkdir('./' + '/report')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = "./report/"+ now +'_'+casesname+".html"
    fp = file(filename, 'wb')
    print 'write report'
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=reporttitle,
        description=reportdescription
    )
    runner.run(cases)
    fp.close()