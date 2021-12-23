import hmac
import hashlib

def hmac_calc(hmac_secret,
              received_hmac,
              amount,
              created_at,
              currency,
              error_occurred,
              has_parent_transaction,
              trx_id,
              integration_id,
              is_3d_secure,
              is_auth,
              is_capture,
              is_refunded,
              is_standalone_payment,
              is_voided,
              order_id,
              owner_id,
              pending,
              source_data_pan,
              source_data_subtype,
              source_data_type,
              success):
    hmac_string= f'{amount}{created_at}{currency}{error_occurred}{has_parent_transaction}{trx_id}{integration_id}{is_3d_secure}{is_auth}{is_capture}{is_refunded}{is_standalone_payment}{is_voided}{order_id}{owner_id}{pending}{source_data_pan}{source_data_subtype}{source_data_type}{success}'

    calculated_hmac= hmac.new(bytes(hmac_secret,'UTF-8'), msg=bytes(hmac_string,'UTF-8'), digestmod= hashlib.sha512).hexdigest()

    if calculated_hmac == received_hmac:
        matching_status = "Successful"
        match= True
    else:
        matching_status = "Failed"
        match= False

    return match, {
        "matching_status": f'{matching_status}',
        "hmac_string":hmac_string,
        "calculated_hmac": f'{calculated_hmac}'
    }
