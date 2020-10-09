from flask import Flask, render_template, request, url_for, redirect
import athletemodel

print('aplle')
print('baaa')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_list', methods=['POST', 'GET'])
def generate_list():
    if request.method == 'POST':
        if request.values['send'] == 'Submit':
            if 'Which_athlete' in request.values:

                return redirect(url_for('generate_timing_data', name=request.values.get('Which_athlete')))
            else:
                return render_template('generate_list.html', alert='請選擇人物啦', names=athletemodel.get_names_from_store())
        elif request.values['send'] == 'creat_athlete':
            dob = request.values['Dob']
            name = request.values['Name']
            athletemodel.add_athlete(name,dob)


    return render_template('generate_list.html', names=athletemodel.get_names_from_store())


@app.route('/generate_timing_data', methods=['POST', 'GET'])
def generate_timing_data():
    athlete_name = request.values.get('name')
    athlete_id = athletemodel.get_ID_from_name(athlete_name)
    athlete = athletemodel.get_athlete_from_id(athlete_id)
    return render_template('generate_timing_data.html', name=athlete['Name'], dob=athlete['DOB'], top3=athlete['top3'],
                           data=athlete['data'])


@app.route('/add_timing_data', methods=['POST', 'GET'])
def add_timing_data():
    athlete_name = request.values.get('name')
    athlete_dob = request.values.get('dob')
    if request.method == 'POST':
        new_time = request.values.get('time')
        id = athletemodel.get_ID_from_name(athlete_name)
        athletemodel.add_time_from_id(id, new_time)
        # return request.values
        return redirect(url_for('generate_timing_data', name=athlete_name))

    return render_template('add_timing_data.html', name=athlete_name, dob=athlete_dob)


@app.route('/create_athlete', methods=['POST', 'GET'])
def create_athlete():
    return render_template('create_athlete.html')


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
