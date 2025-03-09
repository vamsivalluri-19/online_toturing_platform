from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask app
app = Flask(__name__)

# Sample data (could be replaced with a database)
tutors = {
    "tutor1": {"name": "John", "subjects": "Math, Science"},
    "tutor2": {"name": "Alice", "subjects": "English, History"}
}

students = {
    "student1": {"name": "Tom", "progress": "Beginner"},
    "student2": {"name": "Emma", "progress": "Intermediate"}
}

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Tutor Dashboard route
@app.route('/tutor_dashboard')
def tutor_dashboard():
    return render_template('dashboard.html', user_type='tutor', tutors=tutors)

# Student Dashboard route
@app.route('/student_dashboard')
def student_dashboard():
    return render_template('dashboard.html', user_type='student', students=students)

# Start a class (for tutors)
@app.route('/start_class/<tutor_name>', methods=['POST'])
def start_class(tutor_name):
    tutor = tutors.get(tutor_name)
    if tutor:
        return render_template('class.html', tutor=tutor)
    return redirect(url_for('home'))

# Track student progress
@app.route('/track_progress/<student_name>', methods=['POST'])
def track_progress(student_name):
    student = students.get(student_name)
    if student:
        new_progress = request.form.get('progress')
        student['progress'] = new_progress
        return redirect(url_for('student_dashboard'))
    return redirect(url_for('home'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
