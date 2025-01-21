# Jake Wagoner's notes 1/16/25

This mongodb interactor does not provide any data validation. This is simply a proof-of-concept for pulling from a provided JSON file. Any format is able to be inserted into the collection.

Prior to a collection push, there should be a validation step to ensure that the data is formatted in a way that is consistent with prior entires. Additionally, there is some cleanup which should be completed before pushing. A schema should be used/developed for this in order to maintain consistency and cleanliness.