import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DecorComponent } from './decor.component';

describe('decorComponent', () => {
  let component: DecorComponent;
  let fixture: ComponentFixture<DecorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DecorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DecorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
