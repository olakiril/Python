import datajoint as dj

schema = dj.schema('state', locals())

@schema
class Sessions(dj.Manual):
    definition = """
    # Basic Sessions info

    mouse_id                     : int			   # id number
    session_tmst                 : double                  # session timestamp in seconds since the Epoch
    ---
    """

@schema
class Trials(dj.Manual):
    definition = """
    # info about trials

    -> Sessions
    trial_tmst                 : double        # trial tmst
    ---
    stimulus_type              : int           # go - no go
    """

@schema
class Licks(dj.Manual):
    definition = """

    -> Sessions
    lick_tmst			: double 	# lick timestamp
    ---
    """
