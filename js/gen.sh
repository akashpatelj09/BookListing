python csv_saver.py > books.json
dateStamp=$(date)
echo '{"date": "'$dateStamp'"}' > updated_date.json
git add The_Bookworm_Theory_Record.csv
git add books.json
git add updated_date.json
git commit -m "Records updated"
git push
