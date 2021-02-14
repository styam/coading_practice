def transformAttribute(input, *metadata, **args):
    # Sample python transform to pass all attributes through
    final_dict = {
        'region': input.get("region", ""),
        'data': {}
    }
    data_dict = final_dict['data']['ticket'] = {}

    data_dict['subject'] = input.get("subject", "")
    data_dict['description'] = input.get("description", "")
    data_dict['description_text'] = input.get("description_text", "")

    data_dict['due_by'] = input.get("due_by", "")
    data_dict['fr_due_by'] = input.get("fr_due_by")
    data_dict['fr_escalated'] = input.get("fr_escalated", "")
    data_dict['is_escalated'] = input.get("is_escalated", "")
    data_dict['fwd_emails'] = input.get("fwd_emails", "")
    data_dict["email_config_id"] = input.get("email_config_id", "")
    data_dict["sla_policy_id"] = input.get("sla_policy_id", "")
    data_dict['reply_cc_emails'] = input.get("reply_cc_emails", "")
    data_dict['id'] = input.get("id", "")
    data_dict['group_id'] = input.get("group_id", "")
    data_dict['group_name'] = input.get("group_name", "")
    data_dict['department_id'] = input.get("department_id", "")
    data_dict['department_name'] = input.get("department_name", "")
    data_dict['requester_id'] = input.get("requester_id", "")
    data_dict['responder_name'] = input.get("responder_name", "")
    data_dict['status'] = input.get("status", "")
    data_dict['status_name'] = input.get("status_name", "")
    data_dict['priority'] = input.get("priority", "")
    data_dict['priority_name'] = input.get("priority_name", "")
    data_dict['type_name'] = input.get("type", "")
    data_dict['tags'] = []
    data_dict['spam'] = input.get("spam", "")
    data_dict['source'] = input.get("source", "")
    data_dict['source_name'] = input.get("source_name", "")
    data_dict['urgency'] = input.get("urgency", "")
    data_dict['urgency_name'] = input.get("urgency_name", "")
    data_dict['impact'] = input.get("impact", "")
    data_dict['impact_name'] = input.get("impact_name", "")
    data_dict['category'] = input.get("category", "")
    data_dict['sub_category'] = input.get("sub_category", "")
    data_dict['item_category'] = input.get("item_category", "")
    data_dict['cc_emails'] = input.get("cc_emails", "")
    data_dict['created_at'] = input.get("created_at", "")
    data_dict['updated_at'] = input.get("updated_at", "")
    data_dict['attachments'] = input.get("attachments", "")

    custom_dict = {
        "subcontractor_city": {
            "name": "subcontractor_city",
            "label": "Subcontractor City",
        },
        "subcontractor_company": {
            "name": "subcontractor_company",
            "label": "Subcontractor Company",
        },

        "resolution_type": {
            "name": "resolution_type",
            "label": "Resolution Type"
        },
        "resolution": {
            "name": "resolution",
            "label": "Resolution",
        },

        "country": {
            "name": "country",
            "label": "Country",
        },

        "servicezone": {
            "name": "servicezone",
            "label": "Servicezone",
        },

        "status_reson": {
            "name": "status_reason",
            "label": "Subcontractor Company",
        },

        "incident_location": {
            "name": "incident_location",
            "label": "Incident Location",
        },
        "nvr_name": {
            "name": "nvr_name",
            "label": "NVR Name",
        },
        "site_name": {
            "name": "site_name",
            "label": "Site Name",
        },
        "dct": {
            "name": "dct",
            "label": "dct",
        },
        "devices_affected": {
            "name": "devices_affected",
            "label": "Devices Affected",
        },
        "subcontractor_location": {
            "name": "subcontractor_location",
            "label": "Subcontractor Location",
        },
        "billing_status": {
            "name": "billing_status",
            "label": "Billing Status",
        },
        "billing_status_reason": {
            "name": "billing_status_reason",
            "label": "Billing Status Reason",
        },
        "asset_attached": {
            "name": "asset_attached",
            "label": "Asset Attached",
        },
        "resolution_category_method": {
            "name": "resolution_category_method",
            "label": "Resolution Category/Method",
        },
        "destination_ticket": {
            "name": "destination_ticket",
            "label": "Destination Ticket",
        },
        "primary_customer_contact_name": {
            "name": "primary_customer_contact_name",
            "label": "Primary Customer Contact Name",
        },
        "primary_customer_phone_number": {
            "name": "primary_customer_phone_number",
            "label": "Primary Customer Phone Number",
        },
        "region": {
            "name": "region",
            "label": "Region",
        },
        "agent_response": {
            "name": "agent_response",
            "label": "Agent Response",
        },
        "labor_billing_amount": {
            "name": "Labor Billing Amount",
            "label": "Labor Billing Amount",
        },
        "parts_billing_amount": {
            "name": "parts_billing_amount",
            "label": "Parts Billing Amount",
        },
        "alternate_customer_contact_info": {
            "name": "alternate_customer_contact_info",
            "label": "Alternate Customer Contact Info",
        },
        "shipping_billing_amount": {
            "name": "shipping_billing_amount",
            "label": "Shipping Billing Amount",
        },
        "trip_charge_amount": {
            "name": "trip_charge_amount",
            "label": "Trip Charge Amount",
        },
        "repair_charge_amount": {
            "name": "repair_charge_amount",
            "label": "Repair Charge Amount",
        },
        "rental_charges": {
            "name": "rental_charges",
            "label": "Rental Charges",
        },
        "total_billing_amount": {
            "name": "total_billing_amount",
            "label": "Total Billing Amount",
        },
        "billing_notes": {
            "name": "billing_notes",
            "label": "Billing Notes",
        },
        "work_order_number": {
            "name": "work_order_number",
            "label": "Work Order Number",
        },
        "contact_name_for_billing": {
            "name": "contact_name_for_billing",
            "label": "Contact Name For Billing",
        },
        "contact_email_for_billing": {
            "name": "contact_email_for_billing",
            "label": "Contact Email For Billing",
        },
        "strategic_customer": {
            "name": "strategic_customer",
            "label": "Strategic Customer",
        },
        "customer_urgency_request": {
            "name": "strategic_customer",
            "label": "Strategic Customer",
        }

    }

    for(key, value) in custom_dict.items():
        if input["custom_fields"].get(key, None):
            value.update({"value": input["custom_fields"][key]})

    data_dict['custom_fields'] = [custom_dict]

    final_dict['data']['requester'] = {
        "id": input.get("requester_id", ""),
        "name":input.get("name", ""),
        "phone": input.get("phone", ""),
        "email":  input.get("email", ""),
        "mobile": input.get("mobile", ""),
        "created_at": input.get("created_at", "")
    }


    final_dict['assets'] = [
        {
            "name":input.get("name", ""),
            "description": input.get("description", ""),
            "description_text": input.get("description_text", ""),
            "ci_type_id": input.get("ci_type_id", ""),
            "impact": input.get("impact", ""),
            "created": input.get("created", ""),
            "updated": input.get("updated", ""),
            "user_id": input.get("user_id", ""),
            "department_id": input.get("department_id", ""),
            "assigned_on": input.get("assigned_on", ""),
            "agent_id": input.get("agent_id", ""),
            "author_id": input.get("author_id", ""),
            "author_type": input.get("author_type", ""),
            "deleted": input.get("deleted", ""),
            "display_id": input.get("display_id", ""),
            "salvage": input.get("salvage", "")
        }
    ]


    return final_dict

