select distinct A.CAR_ID
from CAR_RENTAL_COMPANY_CAR A, CAR_RENTAL_COMPANY_RENTAL_HISTORY B
where A.CAR_ID=B.CAR_ID 
AND car_type='세단' AND MONTH(start_date)=10
order by CAR_ID DESC