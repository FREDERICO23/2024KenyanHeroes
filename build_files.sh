# build_files.sh
set -x  # Enable debugging
echo "Installing requirements..."
pip install -r requirements.txt
echo "Collecting static files..."
python manage.py collectstatic --noinput