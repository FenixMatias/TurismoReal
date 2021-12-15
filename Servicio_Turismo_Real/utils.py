from .models import Reserva

def get_or_set_reserva_session(request):
	res_id = request.session.get('res_id', None)
	if res_id is None:
		reserva = Reserva()
		reserva.save()
		request.session['res_id'] = reserva.res_id

	else:
		try:
			reserva = Reserva.objects.get(res_id=res_id, res_estado=False)
		except Reserva.DoesNotExist:
			reserva = Reserva()
			reserva.save()
			request.session['res_id'] = reserva.res_id

	if request.user.is_authenticated and reserva.f_use is None:
		reserva.f_use = request.user
		reserva.save()
	return reserva